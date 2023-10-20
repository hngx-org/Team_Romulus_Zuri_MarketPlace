from django.urls import path
from .views import ProductRecommendationView, SimilarProductRecommendationView


urlpatterns = [
    path('recommendations/', ProductRecommendationView.as_view(), name='recommendations'),
    path('similar-products/<uuid:product_id>/', SimilarProductRecommendationView.as_view(), name='similar-products'),
]