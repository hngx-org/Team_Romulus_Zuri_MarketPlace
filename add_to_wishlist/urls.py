from django.urls import path
from .views import  WishlistViewSet


urlpatterns = [
    path('wishlist/', WishlistViewSet.as_view({'post': 'create'}), name='wishlist-create')
]