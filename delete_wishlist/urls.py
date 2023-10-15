from django.urls import path
from .views import DeleteWishlistItem

urlpatterns = [
<<<<<<< HEAD
        path('wishlist/<str:product_id>/<str:userId>', DeleteWishlistItem.as_view(), name='delete_wishlist_item'),
=======
    path('wishlist/delete/<user_id>/<product_id>/', DeleteWishlistItem.as_view(), name='delete_wishlist_item'),
>>>>>>> 34cbe000ac01042469af9e933cd109da2595de10
]
