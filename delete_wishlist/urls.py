from django.urls import path
from .views import DeleteWishlistItem

urlpatterns = [
    path('wishlist/delete/<str:user_id>/<str:product_id>/', DeleteWishlistItem.as_view(), name='delete_wishlist_item'),
]
