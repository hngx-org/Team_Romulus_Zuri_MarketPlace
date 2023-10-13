from django.urls import path
from .views import GetCategoryNames, GetImage, GetProductsSubCategory

urlpatterns = [
        path('categoryNames/', GetCategoryNames.as_view(), name='get_category_names'),
        path('image/<imageId>/', GetImage.as_view(), name='get_images'),
        path('products/<str:categoryName>/<str:subCategory>/', GetProductsSubCategory.as_view(), name='get_products_sub_category'),
]