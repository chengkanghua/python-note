from django.urls import path,re_path
from . import views
urlpatterns = [
    path("image/", views.ImageAPIView.as_view()),
    path("collection/", views.CollecionAPIView.as_view()),
    re_path("^collection/(?P<pk>\d+)/$", views.CollecionDetailAPIView.as_view()),
    path("special/list/", views.SpecialListAPIView.as_view()),
    path("post/special/", views.ArticlePostSpecialAPIView.as_view()),
    re_path("^(?P<pk>\d+)/$", views.ArticleInfoAPIView.as_view()),
]

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register("", views.ArticleAPIView)
urlpatterns += router.urls
