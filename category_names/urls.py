from django.urls import path
from .views import CategoryNameView


urlpatterns = [
    path('category-name/',CategoryNameView.as_view(), name='category_name'),
]