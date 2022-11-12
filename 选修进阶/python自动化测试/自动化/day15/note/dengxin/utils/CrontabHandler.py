# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 8:04
# @Author  : 张开
# File      : CrontabHandler.py


import os
import datetime
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dengxin.settings")

django.setup()



from app01 import models
from utils.RequestHandler import run_case

it_obj = models.It.objects.all()


for i in it_obj:
    if i.it_end_time == datetime.date.today():
        print(i.api_set.all())
        run_case(i.api_set.all())










