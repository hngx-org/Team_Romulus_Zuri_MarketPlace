# delete_wishlist/urls.py
from django.urls import path
from .views import delete_product_from_wishlist

urlpatterns = [
    path('wishlist/<int:product_id>/', delete_product_from_wishlist, name='delete_product_from_wishlist'),
]
