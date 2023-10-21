"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "Zuri Market Place API", 
        default_version = "v1",
        description = "Zuri Marketplace is a place where people who create things like digital items and services can connect with people who want to buy them.", 
        ),
        public = True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/marketplace/v1/', include('recently_viewed.urls')),
    path('api/marketplace/v1/', include('all_products.urls')),
    path('api/marketplace/v1/', include('ProductSubCategory.urls')),
    path('api/marketplace/v1/', include('category_names.urls')),
    

    path('api/marketplace/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/marketplace/v1/', include('product_filter.urls')),
    path('api/marketplace/v1/', include('limited_offer.urls')),
    path('api/marketplace/v1/', include('product_recommendation.urls')),

    path('api/marketplace/v1/', include('product_retrieval.urls')),

    path('api/marketplace/v1/', include('fetch_wishlist.urls')),
    path('api/marketplace/v1/', include('add_to_wishlist.urls')),
    path('api/marketplace/v1/', include('addrecent.urls')),
    path('api/marketplace/v1/', include('product_category.urls')),
    path('api/marketplace/v1/', include('delete_wishlist.urls')),
    path('api/marketplace/v1/', include('product_view.urls')),
]
