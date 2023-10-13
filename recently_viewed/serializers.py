from rest_framework import serializers
from MarketPlace.models import ProductImage
from MarketPlace.models import Shop
from MarketPlace.models import Product
from MarketPlace.models import UserProductInteraction

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('url',)



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('merchant', 'name', 'reviewed', 'rating')



class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    shop = ShopSerializer()

    def get_image_url(self, obj):
        product_image = obj.productimage_set.first()
        return product_image.url if product_image else None

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'quantity', 'category', 'price', 'discount_price', 
                  'tax', 'admin_status', 'is_deleted', 'rating', 'is_published', 'currency', 
                  'createdat', 'updatedat', 'user', 'image_url', 'shop')



class UserProductInteractionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = UserProductInteraction
        fields = ('user', 'product', 'interaction_type', 'createdat')
