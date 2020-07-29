from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, my_logout, user_data_change

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', my_logout, name='logout'),
    path('register/<int:id>/', user_data_change, name='register')
]
