from django.urls import path
from .views import SortProducts

urlpatterns = [
    #path('products/recently-viewed/<user_id>/', GetLastViewedProducts.as_view(), name='get_last_viewed_products'),
     path('products-sort/<str:sorting_option>/', SortProducts.as_view(), name='sort_products'),
]
