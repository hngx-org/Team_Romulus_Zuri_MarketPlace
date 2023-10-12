from rest_framework import serializers
from MarketPlace.models import Product, Shop, UserProductRating, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductImage
		fields = ['url']


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProductRating
		fields = ['rating']


class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
	shop = ShopSerializer(many=False, read_only=True)
	rating = RatingSerializer(many=False, read_only=True)
	# image_set = ProductImageSerializer(many=True, read_only=True)
	images = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Product
		fields = [
			'id', 'shop', 'name', 'description', 'quantity', 'category', 'price', 'images',
			'discount_price', 'tax', 'admin_status', 'is_deleted', 'rating', 'is_published',
			'currency', 'createdat', 'updatedat'
		]

	def get_images(self, obj):
		qs = ProductImage.objects.filter(product=obj)
		return ProductImageSerializer(qs, many=True, context=self.context).data