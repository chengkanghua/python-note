from django.contrib import admin
from django.urls import path, re_path,include

from users.views import index,login,auth
urlpatterns = [
    path("",index),
    path("login/",login),
    path("auth",auth),
]


