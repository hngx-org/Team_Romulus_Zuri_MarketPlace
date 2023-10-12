from rest_framework import serializers
from .models import ProductView
from MarketPlace.models import Product

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
