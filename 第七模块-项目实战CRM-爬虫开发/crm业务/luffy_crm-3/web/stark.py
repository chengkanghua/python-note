#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import site, StarkHandler
from web import models


class SchoolHandler(StarkHandler):
    list_display = ['title']


site.register(models.School, SchoolHandler)


class DepartmentHandler(StarkHandler):
    list_display = ['title', ]


site.register(models.Department, DepartmentHandler)
