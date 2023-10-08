from django.urls import path
from  .views import SimilarProductView, FilterProductView, RecommendationView

urlpatterns = [
    path('similar_products/<uuid:product_id>/', SimilarProductView.as_view(), name='similar-products'),
    path('products/', FilterProductView.as_view(), name='filter_products'),
    path('recommendations/<int:user_id>/', RecommendationView.as_view(), name='recommendations'),
]