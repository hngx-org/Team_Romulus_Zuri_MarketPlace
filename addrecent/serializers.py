from rest_framework import serializers
from MarketPlace.models import UserProductInteraction
from MarketPlace.models import Product
from .currencies import currency_data

class UserProductInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductInteraction
        fields = '__all__'

class ProductItemSerializer(serializers.ModelSerializer):
    currency_symbol = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
			'id', 'shop', 'name', 'description', 'quantity', 'category', 'price',
			'discount_price', 'tax', 'admin_status', 'is_deleted', 'rating', 'is_published',
			'currency', 'currency_symbol', 'createdat', 'updatedat', 'user'
		]

    def get_currency_symbol(self, obj):
        currency_code = getattr(obj, 'currency')#getting the currency code of the product 
        currency_symobol = currency_data.get(currency_code, "$")#getting the corresponding currency symbol default of dollar symbol if the symbol is not found
        return currency_symobol


