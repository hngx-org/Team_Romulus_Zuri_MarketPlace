from django.urls import path
from  .views import SimilarProductView, FilterProductView, GetProductsSubCategories, Status, GetProducts

urlpatterns = [
    path('', Status.as_view(), name='status'),
    path('allProducts', GetProducts.as_view(), name='all_products'),
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('products/<str:category>/<str:subcategory>/', GetProductsSubCategories.as_view(), name='get_products_by_subcategories')
]