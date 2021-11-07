from django.contrib import admin
from django.urls import path, re_path,include

from app01.views import get_timer
urlpatterns = [

    path("timer/", get_timer),
    path("", get_timer),

]