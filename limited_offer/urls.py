# urls.py
from django.urls import path
from .views import LimitedOfferListView

urlpatterns = [
    path('products/limited_offers/', LimitedOfferListView.as_view(), name='limited-offers-list'),
]