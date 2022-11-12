# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 9:37
# @Author  : 张开
# File      : 2. 接口自动化框架开发.py






# import requests
#
# # # 登录
# response = requests.post(url='http://www.neeo.cc:6002/pinter/bank/api/login2', data={"userName": "admin", "password": 1234})
# print(response.json())
#
# cookie = {
#     "www.neeo.cc:6002": {'testfan-id': 'f9dc544f-f3aa-4d7f-8eed-5dfcce01c7e4'},
#     "www.neeo.cc:6003": {'testfan-id': 'f9dc544f-f3aa-4d7f-8eed-5dfcce01c7e4'},
#     "www.neeo.cc:6004": {'testfan-id': 'f9dc544f-f3aa-4d7f-8eed-5dfcce01c7e4'},
#
# }


"""

neeo_001>response_json>data
依赖 neeo_001 用例的 响应json 数据 中的 data 字段

"""
# import re
# import json
# data = json.dumps({"testfan-token": "${neeo_001>response_json>data}$", "userName": "${neeo_001>response_cooies>cookies}$"})
#
# token = '12312313'
#
# pattern = re.compile('\${(.*?)}\$')
# res = pattern.findall(data)
# # print(res)
# for i in res:
#     # print(i)
#     case_num, params, json_path = i.split('>')
#     print(case_num, params, json_path)
#     data = re.sub(pattern, token, data, 1)
#     # break
# print(data)




'''
pip install deepdiff   # 处理数据校验：字符串、字典、图片
pip install jsonpath-rw  # 找路径

'''
#
# from deepdiff import DeepDiff
#
# d1 = {"code": "0", "message": "success"}
# d2 = {"code": "0", "message": "success"}
# d3 = {"code": "1" , "data": "xxxxxxxxxxxx"}
#
# print(DeepDiff(d1, d2).get('values_changed', None))
# print(DeepDiff(d1, d3).get('values_changed', None))

# from deepdiff import grep
#
# obj = {"long": "somewhere", "string": 2, 0: 0, "somewhere": "around", "a": {"b": {"c": {"d": "somewhere"}}}}
# ds1 = obj | grep("somewhere")
# print(ds1)  # {'matched_paths': {"root['somewhere']"}, 'matched_values': {"root['long']", "root['a']['b']['c']['d']"}}
# ds2 = obj | grep("someone")
# print(ds2)  # {}


from jsonpath_rw import parse, parser


json_data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10,
    "category": "xxxxx"
}

rule = "$..category"
match = parse(rule).find(json_data)
print(match)
if match:
    for i in match:
        print(i.value)





































































