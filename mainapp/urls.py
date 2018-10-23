from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='product_index'),

    path('product_list/', views.product_list, name='product_list'),
    path('product_list/product_create/', views.product_create, name='create'),
    path('product_list/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_list/<int:pk>/product_edit/', views.product_edit, name='product_edit'),

    path('category_list/', views.category_list, name='category_list'),
    path('category_list/category_create/', views.category_create, name='category_create'),
    path('category_list/<int:pk>/', views.category_detail, name='category_detail'),
    path('category_list/<int:pk>/category_edit/', views.category_edit, name='category_edit'),

]


