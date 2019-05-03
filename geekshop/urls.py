"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as mainapp_views
from rest_framework.routers import DefaultRouter
from mainapp.api.products import ProductViewSet
from mainapp.api.categories import ProductCategoryViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', ProductCategoryViewSet)

default_router = [
    path('categories/', include('mainapp.endpoints.categories')),
    path('products/', include('mainapp.endpoints.products')),
]

urlpatterns = [
    path('', mainapp_views.main, name='main'),
    path('contacts/', mainapp_views.contacts, name='contacts'),
    path('products/', include('mainapp.urls.products', namespace='products')),
    path('categories/', include('mainapp.urls.categories', namespace='categories')),
    path('default_api/', include(default_router)),
    path('api/', include(router.urls)),
    path('product_info/', mainapp_views.product_info, name='product_info'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
    path('oauth2/', include('social_django.urls', namespace='social')),
    path('cart/', include('cart.urls', namespace='cart')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
