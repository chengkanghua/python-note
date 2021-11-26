#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from app01 import views


class StarkSite(object):
    def __init__(self):
        self._registry = []

    def get_urls(self):
        patterns = []
        """
        patterns = [
            url(r'^index/', views.index),
            url(r'^home/', views.home),
        ]
        """
        for app in self._registry:
            patterns.append(url(r'^%s/' % app, views.index))

        return patterns

    @property
    def urls(self):
        return (self.get_urls(), None, None)


site = StarkSite()
