from django.urls import path
from .views import OrderListView, OrderCreateView

app_name = 'cart'

urlpatterns = [

    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),

]