from django.contrib import admin
from .models import ProductCategory, ProductImage

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(ProductCategory)