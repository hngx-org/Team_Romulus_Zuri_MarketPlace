from django.urls import path
from  .views import SimilarProductView, FilterProductView

urlpatterns = [
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
]