from django.urls import path
from  .views import SimilarProductView

urlpatterns = [
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
]