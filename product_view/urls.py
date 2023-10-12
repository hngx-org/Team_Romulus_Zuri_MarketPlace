from django.urls import path
from .views import GetLastViewedProducts, SortProducts

urlpatterns = [
    path('products/recently-viewed/<user_id>/', GetLastViewedProducts.as_view(), name='get_last_viewed_products'),
    path('products/sort/', SortProducts.as_view(), name='sort-products'),
]
