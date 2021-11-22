#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.conf import settings
from django.shortcuts import HttpResponse


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        验证用户
        :param request:
        :return:
        """
        # 1. 获取白名单，让白名单中的所有url和当前访问url匹配
        for reg in settings.PERMISSION_VALID_URL:
            if re.match(reg, request.path_info):
                return None

        # 2. 获取权限
        permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_list:
            return HttpResponse('无权限信息，请重新登录')

        flag = False
        # 3. 对用户请求的url进行匹配
        for url in permission_list:
            regex = "^%s$" % (url,)
            if re.match(regex, request.path_info):
                flag = True
                break

        if not flag:
            return HttpResponse('无权访问')
