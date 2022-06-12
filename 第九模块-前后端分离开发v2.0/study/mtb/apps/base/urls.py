from django.urls import path
from rest_framework import routers

from .views import account

router = routers.SimpleRouter()

# 其他注册方式
# router.register(r'public',wx.PublicNumberView)

urlpatterns = [
    path('auth/', account.AuthView.as_view()),
    path('test/', account.TestView.as_view()),
]

urlpatterns += router.urls
