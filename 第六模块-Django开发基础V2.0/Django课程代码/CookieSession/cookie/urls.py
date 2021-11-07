from django.contrib import admin
from django.urls import path,include

from cookie import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
]
