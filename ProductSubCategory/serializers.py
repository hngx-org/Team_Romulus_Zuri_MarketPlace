from rest_framework import serializers
from MarketPlace.models import Product, ProductCategory, ProductSubCategory, ProductImage
from category_names.serializers import ProductCategorySerializer

class ProductSerializers(serializers.ModelSerializer):
    #category = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

class ProductsubCatSerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True, read_only=True)

    class Meta:
        model = ProductSubCategory
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = '__all__'
