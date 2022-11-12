# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 15:24
# @Author  : 张开
# File      : ShowTabHandler.py


"""  处理可视化相关 """






import os
import django
import datetime
from datetime import timedelta
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dengxin.settings")
django.setup()


from app01 import models

class ShowTabOpt(object):
    """ 处理图标所需要的数据 """

    def pie(self):
        """ 处理饼图 """
        data = {
            "pass_pie": {
                "title": ["通过", "失败"],
                "data": [
                    {"value": 0, "name": "通过"},
                    {"value": 0, "name": "失败"},
                ]
            },
            "execute_pie": {
                "title": ["已执行", "未执行"],
                "data": [
                    {"value": 0, "name": "已执行"},
                    {"value": 0, "name": "未执行"},
                ]
            }
        }


        # 数据库取数据

        # 法1
        # models.Api.objects.filter(api_pass_status=1).count()
        # models.Api.objects.filter(api_pass_status=0).count()
        # models.Api.objects.filter(api_run_status=1).count()
        # models.Api.objects.filter(api_run_status=0).count()

        # 法2 通过 it 表查

        it_obj = models.It.objects.all()
        for item in it_obj:
            # 已通过
            data["pass_pie"]['data'][0]['value'] += item.api_set.filter(api_pass_status=1).count()
            data["pass_pie"]['data'][1]['value'] += item.api_set.filter(api_pass_status=0).count()
            data["execute_pie"]['data'][0]['value'] += item.api_set.filter(api_run_status=1).count()
            data["execute_pie"]['data'][1]['value'] += item.api_set.filter(api_run_status=0).count()


        print(data)

        return data


    def line_simple(self):
        """ 折线图
        近一年，统计每个月的用例数据走势图（19年5月11号~20年5月11号） 根据 it_start_time 进行过滤
        """
        data_dict = {
                    "line_simple": {
                        "title": [],
                        "data": []
                    }
                }

        end_time = datetime.date.today()
        # 思考，如何获取去年的今天
        start_time = end_time - timedelta(days=365)
        # print(end_time, start_time)
        it_obj = models.It.objects.filter(it_start_time__range=(start_time, end_time))
        # print(it_obj)
        d = {}
        for item in it_obj:
            m = item.it_start_time.strftime("%Y-%m")
            if d.get(m, None): # 月份存在，加value值即可
                d[m] += item.api_set.count()
            else:
                d[m] = item.api_set.count()

        print(d.items())
        # 问题，如何根据字段key排序
        new_d = sorted(d.items(), key=lambda x: x[0])
        print(new_d)
        for i in new_d:
            data_dict['line_simple']['title'].append(i[0])
            data_dict['line_simple']['data'].append(i[1])
        print(data_dict)

        return data_dict
if __name__ == '__main__':
    ShowTabOpt().line_simple()











