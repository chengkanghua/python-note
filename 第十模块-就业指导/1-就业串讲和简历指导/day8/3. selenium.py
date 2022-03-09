# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 14:54
# @Author  : 张开
# File      : 3. selenium.py


# import time
# from selenium import webdriver
# from selenium.webdriver.support.expected_conditions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
#
#
#
# driver = webdriver.Chrome()
#
# # css selector
#
# try:
#     """
#      css selector 能使用：
#         - id
#         - class
#         - tag name
#     """
#     driver.get('http://www.neeo.cc:6005/login/')
#
#     # driver.find_element_by_id('id_username').send_keys('panjingxiang dsb')
#     #
#     # driver.find_element(By.ID, 'id_password').send_keys('10086')
#     #
#     # driver.find_element(By.CSS_SELECTOR, '#id_code').send_keys('xxxxx')
#     # driver.find_element(By.CSS_SELECTOR, 'input#id_code').send_keys('xxxxx')
#
#     # driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('xxxxxx')
#     # driver.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('xxxxxx')
#
#     # print(driver.find_element(By.TAG_NAME, 'input').get_attribute('name'))
#
#     # 支持正则的通配符 ^ $ *
#
#
#     # driver.find_element(By.CSS_SELECTOR, 'input[id ^=id_user]').send_keys('xxxx')
#     # driver.find_element(By.CSS_SELECTOR, 'input[id $=name]').send_keys('xxxx')
#     # driver.find_element(By.CSS_SELECTOR, 'input[id *=erna]').send_keys('xxxx')
#
#     # print(driver.find_element(By.CSS_SELECTOR, 'form input').get_attribute('name'))
#     # print(driver.find_element(By.CSS_SELECTOR, 'form>input').get_attribute('name'))
#     # 更多参考： https://www.cnblogs.com/Neeo/articles/12362920.html#css-selector
#
#     print(driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').value_of_css_property('background-color'))
#
#
#
#
# except NoSuchElementException as e:
#     print(e)
#
# finally:
#     time.sleep(3)
#     driver.quit()
#





import time
import base64
import requests
import unittest
from deepdiff import DeepDiff
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerSelenium import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


"""
登录功能实战
"""


class MyCase(unittest.TestCase):
    user = '张开1'
    password = 'root1234'
    code_img = './code.png'
    url = 'http://www.neeo.cc:6005/login/'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()


    def setUp(self):
        self.driver.get(self.url)

    def test_case_01(self):
        """ 成功 """
        self.driver.find_element(By.ID, 'id_username').send_keys(self.user)
        self.driver.find_element(By.ID, 'id_password').send_keys(self.password)
        # 获取验证码并且使用百度ai的文字识别接口来获取验证码
        self.driver.find_element(By.ID, 'id_code').send_keys(self.get_code())
        # 登录
        self.driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').submit()
        time.sleep(3)
        title = self.driver.title
        # print(111111111111, title, DeepDiff(title, '首页'))
        self.assertEqual(DeepDiff(title, '首页'), {})

    def test_case_02(self):
        """ 失败 """
        self.driver.find_element(By.ID, 'id_username').send_keys(self.user)
        self.driver.find_element(By.ID, 'id_password').send_keys(self.password)
        # 获取验证码并且使用百度ai的文字识别接口来获取验证码
        self.driver.find_element(By.ID, 'id_code').send_keys('xxxx')
        # 登录
        self.driver.find_element(By.CSS_SELECTOR, 'input[type=submit]').submit()
        text = self.driver.find_element_by_xpath('/html/body/div/form/div[3]/div/div[1]/span').text
        # print(222222222222222, text, DeepDiff(text, '验证码输入错误'))
        self.assertNotEqual(DeepDiff(text, '验证码输入错误'), {})


    def get_code(self):
        """ 获取验证码 """
        # 截取验证码图片
        self.driver.find_element_by_id('imageCode').screenshot(self.code_img)
        # 发送验证图片并且获取结果
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        # 二进制方式打开图片文件
        f = open(self.code_img, 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = '24.7653b6be34d6084b8f751ed8584fe5cd.2592000.1592034968.282335-19880823'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()['words_result'][0]['words']
        else:
            return ''



if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=MyCase, prefix='test')
    f = open('./report.html', 'wb')
    HTMLTestRunner(
        stream=f,
        title='S267',
        description='xx00',
        verbosity=2
    ).run(suite)

    f.close()
    # unittest.TextTestRunner(verbosity=2).run(suite)






















