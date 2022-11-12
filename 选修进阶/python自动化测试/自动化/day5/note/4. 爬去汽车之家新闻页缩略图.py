"""
pip install beautifulsoup4



https://www.autohome.com.cn/news/
# 爬取汽车之家新闻页的新闻列表缩略图

# 思路：
1. 访问汽车之家新闻页
2. 定位到缩略图外部的div
3. 获取所有的img标签中的src属性
4. 使用requests模块向img的src地址发请求
5. 保存到本地

"""

import os
import requests
from bs4 import BeautifulSoup  # 解析爬取回来的文本，去其中找标签/标签的属性/标签的内容

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
url = "https://www.autohome.com.cn/news/"
response = requests.request('get', url=url, )
# print(response.encoding)
response.encoding = "GBK"  # 解决乱码问题
# print(response.text)
# 解析文本，拿到解析后的soup对象，所有解析后的数据都在soup对象中
soup_obj = BeautifulSoup(response.text, "html.parser")  # response.text: 要解析的文本    html.parser：指定什么解析器来解析文本
# 使用soup对象找div标签
div_obj = soup_obj.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
# print(div_obj)
# 根据div对象，找其内的所有的img标签
img_list = div_obj.find_all(name="img")
# print(img_list)
for item in img_list:
    img_url = item.get("src")
    if not img_url.startswith("https:"):
        img_url = "https:" + item.get("src")
    img_response = requests.get(img_url)

    file_name = os.path.join(BASE_DIR, 'images', img_url.rsplit("/", 1)[-1])
    with open(file_name, 'wb') as f:
        f.write(img_response.content)
    print(file_name, "download done .........")

# for item in img_list:
#     # print(item)
#     # 获取标签的src属性
#     img_url = "https:" + item.get("src")
#     # 使用requests模块向img url发请求，获取bytes类型数据，并且保存到本地
#     img_response = requests.get(img_url)
#     """
#     https://www3.autoimg.cn/newsdfs/g3/M07/C6/7C/120x90_0_autohomecar__ChsEm16fuVOAbMDxAABrKTBnki8060.jpg
#     """
#
#     file_name = os.path.join(BASE_DIR, 'images', img_url.rsplit("/", 1)[-1])
#     with open(file_name, 'wb') as f:
#         f.write(img_response.content)
#     print(file_name, "download done .........")
#

# h3_list = div_obj.find_all("h3")
# for h3 in h3_list:
#     print(h3.text)
#


"""
pip install beautifulsoup4



https://www.autohome.com.cn/news/
# 爬取汽车之家新闻页的新闻列表缩略图

# 思路：
1. 访问汽车之家新闻页
2. 定位到缩略图外部的div
3. 获取所有的img标签中的src属性
4. 使用requests模块向img的src地址发请求
5. 保存到本地

"""

import os
import requests
from bs4 import BeautifulSoup  # 解析爬取回来的文本，去其中找标签/标签的属性/标签的内容

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
url = "https://www.autohome.com.cn/news/"
response = requests.request('get', url=url, )
# print(response.encoding)
response.encoding = "GBK"  # 解决乱码问题
# print(response.text)
# 解析文本，拿到解析后的soup对象，所有解析后的数据都在soup对象中
soup_obj = BeautifulSoup(response.text, "html.parser")  # response.text: 要解析的文本    html.parser：指定什么解析器来解析文本
# 使用soup对象找div标签
div_obj = soup_obj.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
# print(div_obj)
# 根据div对象，找其内的所有的img标签
img_list = div_obj.find_all(name="img")
# print(img_list)
for item in img_list:
    img_url = item.get("src")
    if not img_url.startswith("https:"):
        img_url = "https:" + item.get("src")
    img_response = requests.get(img_url)

    file_name = os.path.join(BASE_DIR, 'images', img_url.rsplit("/", 1)[-1])
    with open(file_name, 'wb') as f:
        f.write(img_response.content)
    print(file_name, "download done .........")

# for item in img_list:
#     # print(item)
#     # 获取标签的src属性
#     img_url = "https:" + item.get("src")
#     # 使用requests模块向img url发请求，获取bytes类型数据，并且保存到本地
#     img_response = requests.get(img_url)
#     """
#     https://www3.autoimg.cn/newsdfs/g3/M07/C6/7C/120x90_0_autohomecar__ChsEm16fuVOAbMDxAABrKTBnki8060.jpg
#     """
#
#     file_name = os.path.join(BASE_DIR, 'images', img_url.rsplit("/", 1)[-1])
#     with open(file_name, 'wb') as f:
#         f.write(img_response.content)
#     print(file_name, "download done .........")
#

# h3_list = div_obj.find_all("h3")
# for h3 in h3_list:
#     print(h3.text)
#



















