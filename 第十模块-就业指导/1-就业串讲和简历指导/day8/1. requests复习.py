# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 9:08
# @Author  : 张开
# File      : 1. requests复习.py






import requests

# # 登录
response = requests.post(url='http://www.neeo.cc:6002/pinter/bank/api/login', data={"userName": "admin", "password": 1234})
print(response.cookies.get_dict())
# print(response.cookies.items())
#
# # 查询请求依赖登录的cookies
#
# response = requests.get(url='http://www.neeo.cc:6002/pinter/bank/api/query', params={"userName": "admin"}, cookies=response.cookies.get_dict())
# print(response.json())

# file = {"file": open(r'D:\video\20200514串讲\note\_两年测试经验--自动化测试工程师--王xx.doc', 'rb')}
#
# response = requests.post(url='http://www.neeo.cc:6001/post', files=file)
# print(response.json())






# response = requests.get(url='https://www.autohome.com.cn/news/')
# print(response.encoding)
# response.encoding = "GBK"
# print(response.text)
#








