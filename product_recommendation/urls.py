from django.urls import path
from .views import ProductRecommendationView


urlpatterns = [
    path('recommendations/', ProductRecommendationView.as_view(), name='recommendations'),
]