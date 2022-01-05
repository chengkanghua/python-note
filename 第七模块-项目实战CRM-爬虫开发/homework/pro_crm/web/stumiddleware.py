from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect
from django.conf import settings


class StuAuthMiddleware(MiddlewareMixin):
    check_url = settings.STUDENT_AUTH_DIR

    def process_request(self, request):
        print("StuAuthMiddleware request...")
        path = request.path
        if self.check_url in path:
            if not request.session.get('student_info'):
                return HttpResponse('无权限，请登陆')