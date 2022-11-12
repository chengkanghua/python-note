from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect



class LoginValid(MiddlewareMixin):
    print('loginvalid')
    def process_request(self,request,*args,**kwargs):
        # 如果是登陆页面,跳过
        if request.path_info == '/login/':
            return None

        ret = request.session.get("user_info", None)        # 获取用户登录的 session
        if not ret:
             return redirect('/login')

        return None
