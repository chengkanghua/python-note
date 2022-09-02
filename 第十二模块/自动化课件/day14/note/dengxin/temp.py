# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 8:25
# @Author  : 张开
# File      : temp.py



import unittest
from HTMLTestRunner import HTMLTestRunner


class My(unittest.TestCase):

    def test_case(self):
        print(self._testMethodName, self._testMethodDoc)
        self.assertEqual(1, 1)
if __name__ == '__main__':
    f = open('./a.html', 'wb')
    suite = unittest.makeSuite(testCaseClass=My, prefix='test')
    HTMLTestRunner(
        title='aaa',
        stream=f,
        description='bbbb'

    ).run(suite)
