# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 15:12
# @Author  : 张开
# File      : 1. unittest要点.py


import unittest
from HTMLTestRunner import HTMLTestRunner



class MyCase(unittest.TestCase):

    def test_case_01(self):
        self.assertEqual(1, 1)


    def test_case_02(self):
        self.assertEqual(1, 0)

    def test_case_03(self):
        self.assertEqual()



if __name__ == '__main__':
    # 构造 suite
    suite = unittest.makeSuite(testCaseClass=MyCase)
    f = open('./report.html', 'wb')
    result = HTMLTestRunner(
        title='串讲',
        description='26,27测试串讲',
        stream=f,
        verbosity=2
    ).run(suite)

    print(result.__dict__['testsRun'])
    print(result.__dict__['error_count'])
    print(result.__dict__['failure_count'])
    print(result.__dict__['success_count'])













































