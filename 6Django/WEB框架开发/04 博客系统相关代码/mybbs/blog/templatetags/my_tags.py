#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/5/24
from django import template
from blog import models

register = template.Library()


@register.inclusion_tag("panel.html")
def show_panel(username):
    user = models.UserInfo.objects.filter(username=username).first()
    # 拿到当前用户的博客对象
    blog = user.blog
    # 方式一：查询当前站点的文章分类，在前端用连表查询取分类对应的文章数
    # category_list = models.Category.objects.filter(blog=blog)
    # 方式二：利用分组查询出每一个分类以及分类对应的文章数
    from django.db.models import Count
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    print(category_list)
    # 查询当前站点的文章标签
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 按年月归档文章
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"create_ym": "DATE_FORMAT(create_time, '%%Y-%%m')"}
    ).values("create_ym").annotate(c=Count("nid")).values("create_ym", "c")

    return {
        "username": username,
        "category_list": category_list,
        "tag_list": tag_list,
        "archive_list": archive_list
    }
