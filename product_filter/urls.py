from django.urls import path
from .views import FilterProductView


urlpatterns = [
    path('products-filter/', FilterProductView.as_view(), name='filter_products'),
]