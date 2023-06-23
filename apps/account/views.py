from django.contrib.auth import get_user_model
from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.account.serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(
            data=request.data,
            context={'request': request}
        )
        if not serializer.is_valid():
            return Response({"message": serializer.errors}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        user = serializer.validated_data['user']
        token = RefreshToken.for_user(user)
        return Response({
            "refresh": str(token),
            "access": str(token.access_token)
        }, status=status.HTTP_202_ACCEPTED)
