#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings


def init_permission(user, request):
    """
    用户权限初始化
    :param user:
    :param request:
    :return:
    """

    # 根据角色获取所有权限
    permission_list = user.roles.filter(permissions__id__isnull=False).values('permissions__id',
                                                                              'permissions__title',
                                                                              'permissions__url',
                                                                              'permissions__is_menu',
                                                                              'permissions__icon'
                                                                              ).distinct()
    menu_list = []
    permission_url_list = []
    for item in permission_list:
        if item['permissions__is_menu']:
            tmp = {
                'title': item['permissions__title'],
                'icon': item['permissions__icon'],
                'url': item['permissions__url']
            }
            menu_list.append(tmp)

        permission_url_list.append(item['permissions__url'])

    # 将权限信息和菜单信息 放入session
    request.session[settings.MENU_SESSION_KEY] = menu_list
    request.session[settings.PERMISSION_SESSION_KEY] = permission_url_list
