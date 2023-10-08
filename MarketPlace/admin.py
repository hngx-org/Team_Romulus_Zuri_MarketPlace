from django.contrib import admin
from .models import ProductCategory, ProductImage, Product, Shop

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Shop)