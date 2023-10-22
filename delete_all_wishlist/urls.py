from django.urls import path
from .views import DeleteAllWishlistItems

urlpatterns = [
    path('user-wishlist/delete-all/<uuid:user_id>/', DeleteAllWishlistItems.as_view(), name='delete-all-wishlist-items'),
]
