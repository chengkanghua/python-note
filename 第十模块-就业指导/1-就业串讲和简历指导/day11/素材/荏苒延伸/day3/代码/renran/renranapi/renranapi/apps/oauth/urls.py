from django.urls import path
from . import views
urlpatterns = [
    path("qq/url/", views.OAuthQQAPIView.as_view() ),
    path("qq/info/", views.QQInfoAPIView.as_view() ),
    path("qq/login/", views.BindQQUserAPIView.as_view() ),
]