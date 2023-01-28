


from django.contrib import admin
from django.urls import path,include

from users.views import reg,username_auth

urlpatterns = [
    path("reg",reg),
    path("username_auth/",username_auth),
]
