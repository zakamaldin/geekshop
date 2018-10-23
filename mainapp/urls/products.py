from django.urls import path
from mainapp.views import (
    products,
    product_list,
    product_create,
    product_detail,
    product_edit,
)
app_name = 'products'

urlpatterns = [
    path('', products, name='product_index'),

    path('product_list/', product_list, name='product_list'),
    path('product_create/', product_create, name='create'),
    path('product_list/<int:pk>/', product_detail, name='product_detail'),
    path('product_list/<int:pk>/product_edit/', product_edit, name='product_edit'),


]


