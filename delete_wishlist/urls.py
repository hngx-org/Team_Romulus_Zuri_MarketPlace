from django.urls import path
from .views import delete_from_wishlist

urlpatterns = [
    path('wishlist/<uuid:product_id>/', delete_from_wishlist, name='delete_from_wishlist'),
]
