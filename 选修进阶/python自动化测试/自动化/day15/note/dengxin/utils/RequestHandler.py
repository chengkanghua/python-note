# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 8:55
# @Author  : 张开
# File      : RequestHandler.py



"""
处理请求相关和生成测试报告
"""
import os
import json
import unittest
import requests
from deepdiff import DeepDiff
from HTMLTestRunner import HTMLTestRunner
from app01 import models
from dengxin.settings import BASE_DIR



class MyCase(unittest.TestCase):


    def test_case(self):
        """ 用例 """
        self._testMethodName = self.title
        self._testMethodDoc = self.desc
        self.assertEqual(DeepDiff(self.response, self.expect).get('type_changes', None), None, msg=self.msg)


class RequestOperate(object):

    def __init__(self, case_obj):
        self.case_obj = case_obj

    def handler(self):
        """
        关于请求的一些列流程：
            1. 提取case_obj中的字段，使用requests发请求
                1. 对请求参数进行校验
                2. 将请求结果提取出来
            2. 使用unittest进行断言
            3. 更新数据库字段
            4. 将执行结果添加到日志表中
            5. 前端返回
        """
        # 发请求，断言，并生成测试报告
        self.send_msg()
        # 更新数据库字段
        self.update_db_status()


    def send_msg(self):
        """ 发请求 """

        response = requests.request(
            method=self.case_obj.api_method,
            url=self.case_obj.api_url,
            data=self._check_data(),
            params=self._check_params(),
        )
        self.assert_msg(response)

    def assert_msg(self, response):
        """ 处理断言 """
        case = MyCase(methodName='test_case')
        case.response = response.json()
        case.expect = self._check_expect()
        case.msg = "自定义的错误信息: <hr>{}".format(DeepDiff(response.json(), self._check_expect()))
        case.title = self.case_obj.api_name
        case.desc = self.case_obj.api_desc
        suite = unittest.TestSuite()
        suite.addTest(case)
        # unittest.TextTestRunner(verbosity=2).run(suite)
        self.get_report(suite)

    def get_report(self, suite):
        """
        生成用例报告
        :param suite: 用例集
        :return:
        """

        f = open(os.path.join(BASE_DIR, 'a.html'), 'wb')

        # print(suite.countTestCases())
        self.case_result = HTMLTestRunner(
            stream=f,
            verbosity=2,
            title=self.case_obj.api_name,
            description=self.case_obj.api_desc,
        ).run(suite)
        f.close()


    def update_db_status(self):
        """
        更新数据相关字段的状态
            1. api_report
            2. api_run_time
            3. api_pass_status
            4. api_run_status
        """
        # obj = models.Api.objects.filter(pk=self.case_obj.pk).update(
        #     api_report=self.read_file(),
        # )

        # 写报告
        obj = models.Api.objects.filter(pk=self.case_obj.pk).first()
        obj.api_report = self.read_file()

        # 写 执行时间
        import datetime
        obj.api_run_time = datetime.datetime.now()
        # 写 api_run_status
        obj.api_run_status = 1

        # 写 api_pass_status
        log_data = {'pass': 0, "failed": 0, "total": 0, "errors": 0}
        for i in self.case_result.__dict__['result']:
            if i[0]:  # 用例执行失败
                obj.api_pass_status = 0
                log_data['failed'] += 1
            else:
                obj.api_pass_status = 1
                log_data['pass'] += 1
            log_data['total'] += 1
        log_data['errors'] = self.case_result.__dict__['errors'].__len__()
        obj.save()

        # 写log表，通过多少，失败多少，共执行了多少用例
        models.Logs.objects.create(
            log_report=self.read_file(),
            log_sub_it_id=self.case_obj.api_sub_it_id,
            log_pass_count=log_data['pass'],
            log_errors_count=log_data['errors'],
            log_failed_count=log_data['failed'],
            log_run_count=log_data["total"]
        )



    def read_file(self):
        """ 读文件"""
        with open(os.path.join(BASE_DIR, 'a.html'), 'r', encoding='utf-8') as f:
            return f.read()









    def _check_expect(self):
        """ 处理预期值 """
        if self.case_obj.api_expect:
            return json.loads(self.case_obj.api_expect)
        else:
            return {}

    def _check_data(self):
        """
        校验请求的 data 参数 :
            默认，数据库中的data字段是标准的json串
        """
        if self.case_obj.api_data:
            # print(2222222222, json.loads(self.case_obj.api_data))
            return json.loads(self.case_obj.api_data)
        else:
            return {}

    def _check_params(self):
        """
        校验请求的 params 参数 :
            默认，数据库中的 params 字段是标准的json串
        """
        if self.case_obj.api_params:
            return json.loads(self.case_obj.api_params)
        else:
            return {}




def run_case(case_obj):  # ["11", "12"]

    RequestOperate(case_obj=case_obj).handler()















