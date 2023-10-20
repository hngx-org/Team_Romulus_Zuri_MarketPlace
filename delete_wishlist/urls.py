from django.urls import path
from .views import DeleteWishlistItem

urlpatterns = [
    path('users/<user-id>/wishlist/<product-id>/', DeleteWishlistItem.as_view(), name='delete_wishlist_item'),
]
