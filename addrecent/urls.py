from django.urls import path
from . import views

urlpatterns = [
    path('add-recently-viewed/<str:user_id>/<str:product_id>/', views.CreateRecentlyViewd.as_view(), name='recently-viewed'),
]