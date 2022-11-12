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
from io import BytesIO
from deepdiff import DeepDiff
from HTMLTestRunner import HTMLTestRunner
from app01 import models
from dengxin.settings import BASE_DIR


class MyCase(unittest.TestCase):

    def test_case(self):
        """ 用例 """
        # self._testMethodName = self.title
        self._testMethodDoc = self.desc
        self.assertEqual(DeepDiff(self.response, self.expect).get('type_changes', None), None, msg=self.msg)


class RequestOperate(object):

    def __init__(self, case_obj, suite_list):
        self.case_obj = case_obj
        self.suite_list = suite_list

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
        self.suite_list.addTest(case)
        suite = unittest.TestSuite()
        suite.addTest(case)
        self.create_single_report(suite)

    def create_single_report(self, suite):
        """
        生成单个用例报告
        :param suite: 用例集
        :return:
        """
        # f = open(os.path.join(BASE_DIR, 'a.html'), 'wb')
        f = BytesIO()

        # print(suite.countTestCases())
        result = HTMLTestRunner(
            stream=f,
            # verbosity=2,
            title=self.case_obj.api_name,
            description=self.case_obj.api_desc,
        ).run(suite)
        self.update_api_status(result, f)

    def create_m_report(self, suite):
        """
        生成批量用例报告
        :param suite: 用例集
        :return:
        """
        f = BytesIO()
        result = HTMLTestRunner(
            stream=f,
            # verbosity=2,
            title=self.case_obj.api_name,
            description=self.case_obj.api_desc,
        ).run(suite)
        self.update_log_status(result, f)

    def update_log_status(self, result, f):
        """ 更新log表 """
        log_data = {'pass': 0, "failed": 0, "total": 0, "errors": 0}
        for i in result.__dict__['result']:
            if i[0]:  # 用例执行失败
                log_data['failed'] += 1
            else:
                log_data['pass'] += 1
            log_data['total'] += 1
        log_data['errors'] = result.__dict__['errors'].__len__()
        # 写log表，通过多少，失败多少，共执行了多少用例
        models.Logs.objects.create(
            log_report=f.getvalue(),
            log_sub_it_id=self.case_obj.api_sub_it_id,
            log_pass_count=log_data['pass'],
            log_errors_count=log_data['errors'],
            log_failed_count=log_data['failed'],
            log_run_count=log_data["total"]
        )

    def update_api_status(self, result, f):
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
        obj.api_report = f.getvalue()

        # 写 执行时间
        import datetime
        obj.api_run_time = datetime.datetime.now()
        # 写 api_run_status
        obj.api_run_status = 1

        # 写 api_pass_status
        for i in result.__dict__['result']:
            if i[0]:  # 用例执行失败
                obj.api_pass_status = 0
            else:
                obj.api_pass_status = 1
        obj.save()

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


def run_case(api_list):
    """
    批量执行用例，单独执行用例也按照批量执行的来
    :param api_list:
    :return:
    """
    # print(api_list)
    # 在批量执行每一个用例之前创建一个suite_list,然后当批量执行中，执行每一个用例的时候，将封装好的用例对象添加到suite_list中
    # 当批量执行执行完毕后，suite_list中，包含了所有批量执行的用例，此时，在使用HTMLTestRunner去生成一个批量执行的测试报告
    suite_list = unittest.TestSuite()
    for i in api_list:
        RequestOperate(case_obj=i, suite_list=suite_list).handler()
    # 问题，批量执行时，都能单独的执行并且生成各自的测试报告，但如何生成多个用例的报告呢？并且将该报告写入到log表中
    # print(111111111, suite_list)

    RequestOperate(case_obj=i, suite_list=suite_list).create_m_report(suite_list)
