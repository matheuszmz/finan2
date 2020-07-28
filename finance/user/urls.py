from django.urls import path
from django.contrib.auth import views as auth_views
from .views import my_logout

path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout', my_logout, name='logout')
