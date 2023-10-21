from django.urls import path
from .views import WishlistCreateView


urlpatterns = [
    path('user-wishlist/', WishlistCreateView.as_view(), name='wishlist-create')
]