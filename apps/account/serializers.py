from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from apps.account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )
    profile = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'profile')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(
                email=validated_data['email'],
                username=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            profile = Profile.objects.create(
                user=user,
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(self.initial_data.get('password'))
            user.save()
            profile.save()

            return user

    def get_profile(self, obj):
        profile = Profile.objects.filter(user_id=obj.id).first()
        return ProfileSerializer(profile).data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
