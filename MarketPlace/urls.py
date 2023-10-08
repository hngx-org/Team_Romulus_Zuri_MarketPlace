from django.urls import path 
from . import apis as views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/<categories>', views.GetAllCategoriesProduct.as_view)
]