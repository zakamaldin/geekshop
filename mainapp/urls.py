from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.products, name='product_index'),
    path('<int:category_id>/', views.products, name='category'),
]


