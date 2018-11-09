from django.urls import path
from mainapp.api import ProductList

app_name = 'rest_products'

urlpatterns = [

    path('', ProductList.as_view(), name='rest_list'),

]

