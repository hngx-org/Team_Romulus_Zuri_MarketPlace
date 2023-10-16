from rest_framework import serializers
from MarketPlace.models import Product, Wishlist


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)  # Create a nested ProductSerializer field
    
    class Meta:
        model = Wishlist
        fields = '__all__'