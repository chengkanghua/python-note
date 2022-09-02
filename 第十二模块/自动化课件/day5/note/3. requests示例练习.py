import requests




# -------------- 在 get 请求中使用params参数 -------------------------



# response = requests.get(url='http://www.neeo.cc:6001/get?user=zhangkai&pwd=666')
# print(response.json())

# params = {
#     "user": "张开",
#     "pwd": 666
# }
# response = requests.get(url='http://www.neeo.cc:6001/get', params=params)
# print(response.json())




# -------------------- headers --------------------



# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
# }
#
# response = requests.get('https://www.zhihu.com/question/361649589/answer/1163303688', headers=headers)
# print(response.status_code)
# print(response.text)
#



# ---------------- cookies --------------------




# 1. 登录,获取cookies值
data = {
    "userName": "=admin",
    "password": "1234"
}
response = requests.post(url="http://www.neeo.cc:6002/pinter/bank/api/login", data=data)
print(response.json())
print(response.cookies)
print(response.cookies.get_dict())


# 2. 在需要cookies验证的时候，携带上刚才获取到的cookies值
response = requests.get(url='http://www.neeo.cc:6002/pinter/bank/api/query?userName=admin', cookies=response.cookies.get_dict())
print(response.status_code)
print(response.json())




# ------------------------- 文件件下载 ---------------


# response = requests.get('https://www.baidu.com/img/dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif')
# with open("dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif", 'wb') as f:
#     f.write(response.content)



#
# import webbrowser
#
#
# url = 'https://www.baidu.com/img/dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif'
#
# response = requests.get(url=url, stream=True)
# with open('a.gif', 'wb') as f:
#     for chunk in response.iter_content(chunk_size=256):
#         f.write(chunk)
# webbrowser.open('a.gif')


# ---------------- data ------------------

# data = {
#     "userName": "=admin",
#     "password": "1234"
# }
# response = requests.post(url="http://www.neeo.cc:6002/pinter/bank/api/login", data=data)
# print(response.json())
# print(response.cookies)



# ---------------- json -------------


# response = requests.post('http://www.neeo.cc:6001/post', json={"user":"zhangkai"})
# print(response.json())
#

# -------------- 文件上传 ------------------


file = {"file": open('a.gif', 'rb')}
response = requests.post("http://www.neeo.cc:6001/post", files=file)
print(response.json())







