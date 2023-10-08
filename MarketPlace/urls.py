from django.urls import path
from  .views import SimilarProductView, FilterProductView, GetProductsSubCategories

urlpatterns = [
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('api/products/<str:category>/<str:subcategory>/', GetProductsSubCategories.as_view(), name='get_products_by_subcategories')
]