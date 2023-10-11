from django.urls import path, include
from  .views import  ProductListByCategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('products/<str:categories>', ProductListByCategoryView.as_view(), name='get_all_products_by_categories'),
    
]
