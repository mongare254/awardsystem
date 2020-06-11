from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name="home"),
    path('nominate', views.nominate, name="nominate"),
    path('nomin', views.nomin, name="nomin")
]