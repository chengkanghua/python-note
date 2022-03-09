from django.urls import path
from . import views
urlpatterns = [
    path("article/", views.ArticleListAPIView.as_view() ),
]