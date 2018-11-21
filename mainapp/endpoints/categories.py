from django.urls import path
from mainapp.api import CategoryList

app_name = 'rest_categories'

urlpatterns = [

    path('', CategoryList.as_view(), name='rest_list'),

]

