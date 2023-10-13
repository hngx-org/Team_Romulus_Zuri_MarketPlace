from django.urls import path
from .views import ProductSearchView

urlpatterns = [
    path('product-retrieval/', ProductSearchView.as_view(), name='product_search'),
]
