from django.urls import path
from .views import FilterProductView


urlpatterns = [
    path('products/', FilterProductView.as_view(), name='filter_products'),
]