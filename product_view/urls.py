from django.urls import path
from .views import GetLastViewedProducts

urlpatterns = [
    # path('products/recently-viewed/<user_id>/', GetLastViewedProducts.as_view(), name='get_last_viewed_products'),
]
