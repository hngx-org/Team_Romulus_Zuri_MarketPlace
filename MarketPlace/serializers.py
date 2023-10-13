from rest_framework import serializers
from .models import Product, Wishlist, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product_id', read_only=True)  # Create a nested ProductSerializer field
    class Meta:
        model = Wishlist
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
