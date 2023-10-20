from django.urls import path
from . import views

urlpatterns = [
    path('add-recently-viewed/<str:user_id>/<str:product_id>/', views.CreateRecentlyViewd.as_view(), name='recently-viewed'),
    path('get-product/<str:id>/<str:user_id>/', views.GetProductItem.as_view(), name='get-product-item-by-id'),
    path('id-list-products/', views.GetProductByIdList, name='get-product-by-id-list')
]