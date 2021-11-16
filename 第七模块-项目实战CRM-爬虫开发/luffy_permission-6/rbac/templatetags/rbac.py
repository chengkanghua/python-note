#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.template import Library
from django.conf import settings

register = Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    """生成菜单"""

    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    for item in menu_list:
        regex = "^%s$" % (item['url'],)
        if re.match(regex, request.path_info):
            item['class'] = 'active'

    return {
        'menu_list': request.session.get(settings.MENU_SESSION_KEY)
    }
