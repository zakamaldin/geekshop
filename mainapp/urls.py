from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='product_index'),
    path('product_list/', views.product_list, name='list'),
    path('product_list/product_create/', views.product_create, name='create'),
    path('product_list/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_list/<int:pk>/product_edit/', views.product_edit, name='product_edit'),

]


