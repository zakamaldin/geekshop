from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('product_info/', views.product_info, name='product_info'),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
]


