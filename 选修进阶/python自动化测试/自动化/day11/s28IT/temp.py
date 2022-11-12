

#
#
# import requests
#
#
# # r1 = requests.post('http://www.neeo.cc:6002/pinter/bank/api/login', data={"userName": "admin", "password": "1234"})
# # print(r1.cookies.get_dict())
#
# # r2 = requests.get('http://www.neeo.cc:6002/pinter/bank/api/query?userName=admin', cookies=r1.cookies.get_dict())
# r2 = requests.post('http://www.neeo.cc:6001/post', data={"user":"zhangkai", "password":1234, "info": {"address":"beijing", "phone":10086}})
# print(r2.json())


from deepdiff import DeepDiff






data = {'code': '1', 'message': 'success'}
response_json = {'code': '0', 'data': 'c03d4a1ef6d34ccdbebbe1b6fd72ca31'}


d1 = {"a": 1, "b": 2, "c": 3, 'e': {"a": 2}}
d2 = {"a": 1, "b": 2, "c": 3, "d": 4, 'e': {"a": 1}}


# print(DeepDiff(d1, d2))
print(DeepDiff(data, response_json))





