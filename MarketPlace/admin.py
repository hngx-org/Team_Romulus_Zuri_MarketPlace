from django.contrib import admin
from .models import ProductCategory, ProductImage, Product, Shop, Wishlist, User

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Wishlist)
admin.site.register(User)