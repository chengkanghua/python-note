"""
@FileName：case_set.py
@Author：chengkanghua
@Time：2022/8/30 11:12 上午
"""

import requests
from bs4 import BeautifulSoup
class CaseSet(object):
    def get_status_code(self,url=None):
        '''用于返回 状态码'''
        return requests.get(url="https://www.baidu.com").status_code

    def get_json_data(self, url="http://www.neeo.cc:6001/get?k1=v1"):
        """ 返回json数据 """
        return requests.get(url).json()

    def get_text_data(self, url=None):
        """ 返回页面的title """
        response = requests.get(url="https://www.baidu.com")
        response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(response.encoding)
        return soup.find(name="title").text


