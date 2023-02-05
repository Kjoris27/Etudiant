import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('base/, views.base, name = 'base'),
    path('home/, views.home, name ='home'),
]
