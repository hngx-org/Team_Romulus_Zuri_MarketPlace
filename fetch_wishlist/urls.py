from django.urls import path
from .views import WishlistProductsView


urlpatterns = [
    path('user-wishlist/<user_id>/', WishlistProductsView.as_view(), name='get_user_wishlist')


]