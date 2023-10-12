from django.urls import path
from recently_viewed.views import RecentlyViewedProducts

urlpatterns = [
    path('recently-viewed/<user_id>/', RecentlyViewedProducts.as_view(), name='recently-viewed'),
]