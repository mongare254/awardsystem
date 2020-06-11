from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepanel'),
    path('history/',views.history,name='history'),
    path('submit/',views.submit,name='submit')
]