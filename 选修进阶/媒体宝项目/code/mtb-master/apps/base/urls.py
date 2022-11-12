from django.urls import path
from rest_framework import routers

from .views import account
from .views import wx
from .views import upload

router = routers.SimpleRouter()

# 其他注册方式
router.register(r'public', wx.PublicNumberView)

urlpatterns = [
    path('auth/', account.AuthView.as_view()),
    path('test/', account.TestView.as_view()),
    path('wxurl/', wx.WxUrlView.as_view()),
    path('wxcallback/', wx.WxCallBackView.as_view(), name='wx_callback'),
    path('upload/', upload.UploadImageView.as_view()),
]

urlpatterns += router.urls
