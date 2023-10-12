from django.contrib import admin
from .models import ProductCategory, ProductImage, Product, Shop, Wishlist, User, ProductSubCategory, UserProductRating

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(UserProductRating)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Wishlist)
admin.site.register(User)