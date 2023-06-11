from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayMainpage, name = 'mainpage'),
]