





```python


# import requests
# # response = requests.request(method='post', url='http://www.neeo.cc:6002/pinter/bank/api/login2', data={"userName":"admin", "password":1234})
# # data = response.json()
#
# response = requests.request(method='post', url='http://www.neeo.cc:6002/pinter/bank/api/login2', data={"userName":"admin", "password":1234})
#
# data = response.json()
# print(data)
# response = requests.request(method='get', url='http://www.neeo.cc:6002/pinter/bank/api/query2', params={"userName": "admin"},
#                             headers={"testfan-token": data['data']}
#                             )
# print(response.json())

data = {
    'code': '0',
    'message': 'success',
    'data': '95e947dd5a684105b97cf74d3a4514a8',
    "info": {
        "address": "北京",
        "phone": "1212313123"
    },
    "item": [
        {"user": "zhangkai"},
        {"user": "wuaihua"},
    ],
    "userName": "zhangkai",
    "password": 1234,
}

# print(data['info']['phone'])
# a = 'info.address'
a = 'item.[1].user'
# a = '$..user'


from jsonpath_rw import parse
#
# js_exe = parse(a)
# match = js_exe.find(data)
# print([i.value for i in match])

import re
import json
data2 = {
    "userName": "${neeo_002>params>userName}$",
    "password": "${neeo_003>data>password}$",
    "user": "${neeo_003>data>item.[0].user}$"
}

pattern = re.compile('\${(.*?)}\$')
match_list = pattern.findall(json.dumps(data2))
print(match_list)
for i in match_list:
    case, params, json_path = i.split(">")
    print(case, params, json_path)
    match = parse(json_path).find(data)
    temp = [v.value for v in match][0]
    # re.match(json_path, json.dumps(data2), temp)
    data2= re.sub(pattern, temp, json.dumps(data2), 1)
    print(data2)
    # break

"""
JsonPath

pip install jsonpath-rw



正则匹配： ${neeo_001>data>data.info.address.phone}$   --> neeo_001>data>data.info.address.phone  --> abc

正则替换：${neeo_001>data>data.info.address.phone}$ --> abc

abc
${}$
${neeo_001>data>data.info.address.phone}$
abc
${neeo_001>headers>data}$
${neeo_001>params>data}$

neeo_001 data data.info.address.phone
    - neeo_001:依赖数据来自于哪个用例
    - data: 来自于哪个用例中的什么参数：
        - response.json
        - headers
        - cookies
        - params
    - data.info.address.phone: 数据所在的路径

neeo_001 data data
case_num 

"""

```







# 处理cookie的思路

思路：

1.  在每个用例发请求的时候，查看响应结果是否有cookies返回
2.  如果有cookie返回，就把保存起来
    1.  保存到本的指定目录，以域名命名，当有接口需要cookies的时候，去指定目录里根据域名匹配查找cookies，然后携带。
    2.  将cookies保存到当前的用例对象中，可以为用例对象新建一个临时字段，来保存cookies，谁要用，就来找就完了。



**问题：如何获取域名？**

```python
从url上切
```



































