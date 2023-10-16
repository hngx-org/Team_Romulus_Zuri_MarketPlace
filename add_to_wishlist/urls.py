from django.urls import path
from .views import  WishlistCreateView


urlpatterns = [
    path('wishlist/', WishlistCreateView.as_view(), name='wishlist-create')
]