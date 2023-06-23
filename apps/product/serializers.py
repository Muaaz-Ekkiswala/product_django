from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.product.models import Product, ProductDetails, Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ("id", "name")


class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetails
        fields = ('id', 'quantity', 'description', 'category')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price')

    def create(self, validated_data):

        product_detail = {
            "description": self.initial_data.get('description'),
            "quantity": self.initial_data.get('quantity'),
            "category" : self.initial_data.get('category'),
        }
        product_detail_data = ProductDetailsSerializer(data=product_detail)
        if not product_detail_data.is_valid():
            raise ValidationError(product_detail_data.errors)
        product = Product.objects.create(**validated_data)
        product_detail_data.save(product=product)
        return product

    def update(self, instance, validated_data):
        product_detail_instance = ProductDetails.objects.filter(product=instance).first()
        product_detail = {
            "description": self.initial_data.get('description') or product_detail_instance.description,
            "quantity": self.initial_data.get('quantity') or product_detail_instance.quantity,
        }
        product_detail_data = ProductDetailsSerializer(data=product_detail)
        if not product_detail_data.is_valid():
            raise ValidationError(product_detail_data.errors)
        product_detail_data.save(product=instance)
        return super().update(instance, validated_data)

