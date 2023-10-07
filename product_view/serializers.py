from rest_framework import serializers
from .models import ProductView

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = '__all__'