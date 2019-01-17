from django.urls import path
from mainapp.api import ProductList, ProductViewSet

app_name = 'rest_products'

urlpatterns = [

    path('', ProductList.as_view(), name='rest_list'),
    # path('', ProductViewSet, name='new_rest_list'),


]

