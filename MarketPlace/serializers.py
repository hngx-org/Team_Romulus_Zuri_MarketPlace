from rest_framework import serializers
from .models import Product, Wishlist, WishListItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class WishListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishListItem
        fields = '__all__'

