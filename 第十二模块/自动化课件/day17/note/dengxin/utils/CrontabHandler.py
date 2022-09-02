# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 8:45
# @Author  : 张开
# File      : CrontabHandler.py

import os
import django
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dengxin.settings")

django.setup()



from app01 import models
from utils.RequestHandler import run_case

def job1():
    """ 定时任务的逻辑实现  """
    # 循环 it 表的 it_end_time 字段，判断该字段的值是否是当天，如果是当天的，就执行其内的所有用例
    it_obj = models.It.objects.all()
    today = datetime.date.today()
    for item in it_obj:
        if item.it_end_time == today:
            run_case(item.api_set.all())

def foo():
    scheduler = BlockingScheduler()
    scheduler.add_job(job1, 'interval', seconds=10, id='job1')  # 每隔5秒执行一次
    scheduler.start()

if __name__ == '__main__':
    job1()





















