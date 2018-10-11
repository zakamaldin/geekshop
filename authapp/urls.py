from django.urls import path
from authapp import views as authapp

app_name = 'auth'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('edit/', authapp.logout, name='edit'),
    path('register/', authapp.logout, name='register'),


]


