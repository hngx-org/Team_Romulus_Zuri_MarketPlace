from rest_framework import serializers
from all_products.serializers import AllProductSerializer
from MarketPlace.models import Wishlist, User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("id", "username", "email")
        ref_name = 'user_wishlist'

class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    product = AllProductSerializer(many=False, read_only=True)

    class Meta:
        model = Wishlist
        fields = ("id", "user", "product", "createdat", "updatedat")