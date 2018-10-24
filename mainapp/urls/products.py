from django.urls import path
from mainapp.views import (
    products,
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView
)
app_name = 'products'

urlpatterns = [
    path('', products, name='product_index'),

    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='create'),
    path('product_list/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_list/<int:pk>/product_edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product_list/<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),



]


