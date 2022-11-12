"""mybbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views, urls as blog_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reg/', views.reg),
    url(r'^login/', views.login),
    url(r'^login2/', views.login2),
    url(r'^logout/', views.logout),
    url(r'^index/', views.index),

    # 上传文件
    url(r'upload_img/', views.upload_img),

    url(r'^test/', views.test),

    url(r'^get_valid_pic/', views.get_valid_pic),
    # 滑动验证码
    url(r'^pc-geetest/register', views.pc_get_captcha),
    # blog子路由
    url(r'blog', include(blog_urls)),
    # media
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    
    # api
    url(r'^demo', views.demo),
    url(r'^api/tags/', views.tags),
    url(r'^$', views.index),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
