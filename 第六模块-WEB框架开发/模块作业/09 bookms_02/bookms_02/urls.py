"""bookms_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,path


from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',views.login),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/', views.register),
    re_path('publish/$', views.publish),
    re_path('publish/delete/(?P<id>\d+)/', views.del_publish),
    re_path('authors/$', views.authors),
    re_path('author/delete/(?P<id>\d+)/', views.del_author),
    re_path('books/$', views.books),
    re_path('books/(?P<condition>publish|author)/(?P<param>.*)/$',views.books),
    re_path('books/add/$', views.add_book),
    re_path('books/change',views.change_books),
    # re_path('books/(\d+)/change/$', views.change_book),
    re_path('books/(\d+)/delete/$', views.delete_book),



]
