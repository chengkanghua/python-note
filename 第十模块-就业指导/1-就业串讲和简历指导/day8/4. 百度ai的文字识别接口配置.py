# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 15:49
# @Author  : 张开
# File      : 4. 百度ai的文字识别接口配置.py



"""
1. 使用百度ai的账号（百度网盘的账号/百度云）登录百度AI的控制台 https://ai.baidu.com/
2. 选择文字识别功能，创建一个文字识别的应用，API Key和Secret Key
3. 获取access_token
4. 配置文字识别接口所需要的配置后，发送图片并且获取结果

"""

import base64
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=DFxepfztRGV2pbLUyVP8Bzqg&client_secret=jjbgduk9Nq222fEqrShHRFA6DIigug2c'
# response = requests.get(host)
# if response:
#     print(response.json()['access_token'])

'''
通用文字识别
'''

# 获取 imageCode

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.neeo.cc:6005/login/')
#
# driver.find_element_by_id('imageCode').screenshot('a.png')



request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('./a.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.7653b6be34d6084b8f751ed8584fe5cd.2592000.1592034968.282335-19880823'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json()['words_result'][0]['words'])