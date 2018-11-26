from django.urls import path
from authapp import views as authapp
from .views import RegisterView

app_name = 'auth'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('edit/', authapp.edit, name='edit'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('register/', authapp.account_signin, name='register'),
    path('verify/<str:email>/<str:activation_key>/', authapp.verify, name='verify'),


]


