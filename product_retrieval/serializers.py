from rest_framework import serializers
from MarketPlace.models import Product

class ProductSerializer(serializers.ModelSerializer):
    highlighted_name = serializers.CharField(read_only=True, required=False)  # added
    highlighted_description = serializers.CharField(read_only=True, required=False)  # added
    
    class Meta:
        model = Product
        fields = '__all__'
