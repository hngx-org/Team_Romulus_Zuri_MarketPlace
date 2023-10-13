from django.urls import path
from .views import ProductListAPIView


urlpatterns = [
	path('product-list/', ProductListAPIView.as_view()),
]