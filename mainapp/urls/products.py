from django.urls import path
from mainapp.views import (
    products,
    ProductListView,
    ProductCreateView,
    product_detail,
    product_edit,
)
app_name = 'products'

urlpatterns = [
    path('', products, name='product_index'),

    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='create'),
    path('product_list/<int:pk>/', product_detail, name='product_detail'),
    path('product_list/<int:pk>/product_edit/', product_edit, name='product_edit'),


]


