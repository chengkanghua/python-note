from django.urls import path,re_path
from . import views
urlpatterns = [
    path("alipay/", views.AliPayAPIView.as_view()),
    path("alipay/result/", views.AlipayResultAPIView.as_view()),
]

