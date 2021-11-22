#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from django.template import Library
from django.conf import settings
from collections import OrderedDict

register = Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    """生成菜单"""

    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    key_list = sorted(menu_dict)

    ordered_dict = OrderedDict()
    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'
        for per in val['children']:
            regex = "^%s$" % (per['url'],)
            if re.match(regex, request.path_info):
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val
    return {
        'menu_dict': ordered_dict
    }
