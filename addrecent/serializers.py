from rest_framework import serializers
from MarketPlace.models import UserProductInteraction
from MarketPlace.models import Product,ProductImage, User, Shop
from .currencies import currency_data
from rest_framework.response import Response
from all_products.serializers import AllProductImageSerializer

class UserProductInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductInteraction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Shop
        fields = '__all__'
    
   

class ProductItemSerializer(serializers.ModelSerializer):
    currency_symbol = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer()
    shop = ShopSerializer()
    
    
    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'description', 'quantity', 'category', 'price', 'images', 'discount_price', 'tax', 'admin_status', 'is_deleted', 'rating', 'is_published', 'currency', 'currency_symbol', 'createdat', 'updatedat', 'user']

    def get_currency_symbol(self, obj):
        #getting the currency code of the product
        currency_code = getattr(obj, 'currency')
        #changing the currency code to string and then to uppercase
        currency_code = str(currency_code).upper()
        return currency_data.get(currency_code, "$")

    def get_images(self, obj):
        qs = ProductImage.objects.filter(product=obj)
        return AllProductImageSerializer(qs, many=True, context=self.context).data
    
    

