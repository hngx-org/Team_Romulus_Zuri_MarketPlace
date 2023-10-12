from django.urls import path
from .views import GetCategoryNames, GetImage, GetProductsSubCategory

urlpatterns = [
        path('categoryNames', GetCategoryNames.as_view(), name='category-names'),
        path('image/<imageId>', GetImage.as_view(), name='images'),
        path('products/<str: categoryName>/<str: subCategoryName>', GetProductsSubCategory.as_view(), name='product-sub-category'),

]
