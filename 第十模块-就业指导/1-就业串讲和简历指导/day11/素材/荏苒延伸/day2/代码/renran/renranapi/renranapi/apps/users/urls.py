from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views
urlpatterns = [
    path("login/", obtain_jwt_token),
    path("captcha/", views.CaptchaAPIView.as_view() ),
    path("", views.UserCreateAPIView.as_view()),
    re_path("sms/(?P<mobile>1[3-9]\d{9})/", views.SMSCodeAPIView.as_view()),
    path("find/password/", views.ResetPasswordAPIView.as_view() ),
    path("follow/", views.FollowAPIView.as_view() ),
    re_path("(?P<pk>\d+)/" ,views.UserCenterAPIView.as_view() ),
    path("record/", views.UserRecordAPIView.as_view()),
]