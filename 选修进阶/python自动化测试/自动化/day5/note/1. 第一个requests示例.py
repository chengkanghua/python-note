

"""
pip install requests

"""

import requests


# response = requests.get('https://www.baidu.com/img/dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.gif')
# response = requests.get('https://www.cnblogs.com/Neeo/articles/11511087.html#requestsrequest')
response = requests.get('http://www.neeo.cc:6002/pinter/com/getSku?id=1')
# print(response.status_code)  # cha
# print(response.content)  # 查看bytes类型的数据，通常是获取图片
print(response.headers)   # 查看响应头
print(response.json())

# with open("dongdiqiu_e991bad6a2fe51ffcdaf1db6d5cb0e36.html", 'w', encoding='utf-8') as f:
#     f.write(response.text)
