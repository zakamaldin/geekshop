from django.urls import path
from mainapp.views import (
    ProductCategoryListView,
    ProductCategoryCreateView,
    ProductCategoryDetailView,
    ProductCategoryUpdateView,
    ProductCategoryDeleteView,
)
app_name = 'categories'

urlpatterns = [

    path('', ProductCategoryListView.as_view(), name='category_list'),
    path('category_create/', ProductCategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/', ProductCategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/category_edit/', ProductCategoryUpdateView.as_view(), name='category_edit'),
    path('<int:pk>/category_delete/', ProductCategoryDeleteView.as_view(), name='category_delete'),

]

