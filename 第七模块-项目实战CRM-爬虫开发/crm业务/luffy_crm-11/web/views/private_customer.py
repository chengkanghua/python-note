#!/usr/bin/env python
# -*- coding:utf-8 -*-
from stark.service.v1 import StarkHandler


class PrivateCustomerHandler(StarkHandler):
    list_display = ['name', ]
