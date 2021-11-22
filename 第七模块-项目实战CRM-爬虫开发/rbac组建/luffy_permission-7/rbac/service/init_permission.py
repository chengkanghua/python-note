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
                                                                              'permissions__menu_id',
                                                                              'permissions__menu__title',
                                                                              'permissions__menu__icon',
                                                                              ).distinct()

    menu_dict = {}
    permission_url_list = []
    for item in permission_list:
        permission_url_list.append(item['permissions__url'])
        menu_id = item['permissions__menu_id']
        if not menu_id:
            continue

        node = {
            'title': item['permissions__title'],
            'url': item['permissions__url']
        }
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [
                    node
                ]
            }

    # 将权限信息和菜单信息 放入session
    request.session[settings.MENU_SESSION_KEY] = menu_dict
    request.session[settings.PERMISSION_SESSION_KEY] = permission_url_list
