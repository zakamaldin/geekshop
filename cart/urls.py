from django.urls import path
from .views import (
    OrderListView,
    OrderCreateView,
    cart_view
)

app_name = 'cart'

urlpatterns = [

    path('', cart_view, name='cart'),
    path('list/', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),

]