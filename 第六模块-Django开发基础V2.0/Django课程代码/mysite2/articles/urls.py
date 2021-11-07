
from django.contrib import admin
from django.urls import path, re_path,include

from articles.views import article_archive_by_year,article_archive_by_month

urlpatterns = [

    re_path("(\d{4})$", article_archive_by_year),  # article_archive_by_year(request,2010)
    re_path("(?P<year>\d{4})/(?P<month>\d{1,2})", article_archive_by_month),

]