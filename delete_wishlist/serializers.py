# delete_wishlist/serializers.py
from rest_framework import serializers
from MarketPlace.models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
