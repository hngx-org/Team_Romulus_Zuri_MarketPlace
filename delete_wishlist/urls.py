from django.urls import path
from .views import DeleteWishlistItem, DelAll

urlpatterns = [
    path('user-wishlist/<user_id>/<product_id>/', DeleteWishlistItem.as_view(), name='delete_wishlist_item'),
    path('user-wishlist/user/<str:user_id>', DelAll.as_view(), name='delete-all-wishlist'),
]
