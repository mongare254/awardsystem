from django.urls import  path
from . import views

app_name='auth'
urlpatterns = [
    path('login/', views.loginuser,name='login'),
    path('logout/', views.logout_user,name='logoutuser')
    ]