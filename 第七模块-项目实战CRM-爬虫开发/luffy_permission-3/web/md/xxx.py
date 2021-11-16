#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息校验
    """

    def process_request(self, request):
        """
        当用户请求刚进入时候出发执行
        :param request:
        :return:
        """

        """
        1. 获取当前用户请求的URL
        2. 获取当前用户在session中保存的权限列表 ['/customer/list/','/customer/list/(?P<cid>\\d+)/']
        3. 权限信息匹配
        """
        # 白名单
        valid_url_list = [
            '/login/',
            '/admin/.*',
            '/logout/',
        ]

        current_url = request.path_info  # 当前访问url地址
        # print(current_url)
        # print(request.session['luffy_permission_url_list_key'])  # ['/customer/list/', '/customer/add/', '/customer/del/(?P<cid>\\d+)/'...]
        # print(request.session.get('luffy_permission_url_list_key',None))
        # print(request.session.keys())   # dict_keys(['luffy_permission_url_list_key']) # session_data里的key
        # print(request.session.values()) # dict_values([['/customer/list/', '/customer/add/', '/customer/del/(?P<cid>\\d+)/', '/customer/edit/(?P<cid>\\d+)/', '/customer/import/', '/customer/tpl/', '/payment/list/', '/payment/add/', '/payment/del/(?P<pid>\\d+)/', '/payment/edit/(?P<pid>\\d+)/']])
        # print(request.session.items())  # dict_items([('luffy_permission_url_list_key', ['/customer/list/', '/customer/add/', '/customer/del/(?P<cid>\\d+)/', '/customer/edit/(?P<cid>\\d+)/', '/customer/import/', '/customer/tpl/', '/payment/list/', '/payment/add/', '/payment/del/(?P<pid>\\d+)/', '/payment/edit/(?P<pid>\\d+)/'])])
        # print(request.session.session_key) # x9oeawizhg9iymvm6l3c5lrhoc2eoo8t # 这个是数据库中 session_key
        for valid_url in valid_url_list:
            if re.match(valid_url, current_url):
                # 白名单中的URL无需权限验证即可访问
                return None

        permission_list = request.session.get('luffy_permission_url_list_key')
        if not permission_list:
            return HttpResponse('未获取到用户权限信息，请登录！')

        flag = False

        for url in permission_list:
            # print(url)
            reg = "^%s$" % url
            if re.match(reg, current_url):
                flag = True
                break

        if not flag:
            return HttpResponse('无权访问')
