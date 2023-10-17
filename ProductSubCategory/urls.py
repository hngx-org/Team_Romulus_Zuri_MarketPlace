from django.urls import path
from .views import GetCategoryNames, GetImages, GetProductsSubCategory, subCat

urlpatterns = [
        path('categoryNames/', GetCategoryNames.as_view(), name='category-names'),
        path('product/<str:cat>/<str:Subcat>', subCat.as_view(), name='subcat'),
        path('image/<productId>/', GetImages.as_view(), name='product-images'),
        path('images/', GetImages.as_view(), name='product-images'),
        path('products/<str:category>/<str:subcategory>/', GetProductsSubCategory.as_view(), name='product-sub-category'),
        # not working yet

]
