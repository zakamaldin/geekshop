from django.urls import path
from mainapp.api import ProductList, product_json_list

app_name = 'rest_products'

urlpatterns = [

    path('', ProductList.as_view(), name='rest_list'),
    path('new_api/', product_json_list, name='new_rest_list'),

]

