from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from authDemo import settings

class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        white_list=settings.WHITE_LIST   #白名单
        if request.path in white_list:   #白名单不做处理
            return None
        if not request.user.is_authenticated:
            return redirect("/login/")

