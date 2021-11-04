#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/5/23

import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybbs.settings")
    import django
    django.setup()

    # MySQL: DATE_FORMAT(data, fmt)
    # SQLite: strftime(fmt, date)
    from django.db.models import Count
    from blog import models
    # 给每一个文章对象加一个hehe字段
    # ret = models.Article.objects.all().extra(
    #     select={"hehe": "create_time > '2017-05-10'"}
    # )
    # print(ret)

    # 查询每一个年月对应的文章数
    ret = models.Article.objects.extra(
        select={"create_ym": "DATE_FORMAT(create_time, '%%Y-%%m')"}
    ).values("create_ym").annotate(c=Count("nid")).values("create_ym", "c")
    for i in ret:
        print(i)
