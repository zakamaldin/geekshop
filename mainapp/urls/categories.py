from django.urls import path
from mainapp.views import (
    category_list,
    category_create,
    category_detail,
    category_edit,
)
app_name = 'categories'

urlpatterns = [

    path('category_list/', category_list, name='category_list'),
    path('category_create/', category_create, name='category_create'),
    path('category_list/<int:pk>/', category_detail, name='category_detail'),
    path('category_list/<int:pk>/category_edit/', category_edit, name='category_edit'),

]

