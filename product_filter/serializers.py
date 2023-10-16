from rest_framework import serializers
from MarketPlace.models import Product, Shop, UserProductRating, ProductImage, ProductCategory, ProductSubCategory


class AllProductImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductImage
		fields = ['url']


class AllRatingSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProductRating
		fields = ['rating']
		

class AllSubCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductSubCategory
		fields = ['name']
		

class AllCategorySerializer(serializers.ModelSerializer):
	sub_category = AllSubCategorySerializer(many=False, read_only=True)

	class Meta:
		model = ProductCategory
		fields = ['id', 'name', 'sub_category']


class AllShopSerializer(serializers.ModelSerializer):

	class Meta:
		model = Shop
		fields = ['id', 'name']


class AllProductSerializer(serializers.ModelSerializer):
	shop = AllShopSerializer(many=False, read_only=True)
	rating = AllRatingSerializer(many=False, read_only=True)
	# image_set = AllProductImageSerializer(many=True, read_only=True)
	images = serializers.SerializerMethodField(read_only=True)
	category = AllCategorySerializer(many=False, read_only=True)
	#sub_category = AllSubCategorySerializer(many=False, read_only=True)
	
	class Meta:
		model = Product
		fields = [
			'id', 'shop', 'name', 'description', 'quantity', 'category', 'price', 'images',
			'discount_price', 'tax', 'admin_status', 'is_deleted', 'rating', 'is_published',
			'currency', 'createdat', 'updatedat'
		]

	def get_images(self, obj):
		qs = ProductImage.objects.filter(product=obj)
		return AllProductImageSerializer(qs, many=True, context=self.context).data