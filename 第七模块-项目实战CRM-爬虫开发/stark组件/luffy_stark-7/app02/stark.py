#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app02 import models


class HostHandler(StarkHandler):
    list_display = ['id', 'host', StarkHandler.display_edit]


site.register(models.Host, HostHandler)

site.register(models.Role, StarkHandler)

site.register(models.Project, StarkHandler)
