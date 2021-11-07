from django.contrib import admin
from django.urls import path,include

from session import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('shop', views.shop),
]
