

import unittest
from HTMLTestRunner import HTMLTestRunner

class MyCase(unittest.TestCase):


    def test_case_01(self):
        self.assertTrue(1)

    def test_case_02(self):
        self.assertTrue("")

    def test_case_03(self):
        self.assertTrue(0)


if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=MyCase)
    # print(suite)

    f = open('./result.html', 'wb')

    HTMLTestRunner(
        stream=f,
        title='s28第一个unittest测试用例',
        description="s28的测试报告",
        verbosity=2

    ).run(suite)

    # BSTestRunner(
    #     stream=f,
    #     title='s28第一个unittest测试用例',
    #     description="s28的测试报告",
    #     verbosity=2
    #
    # ).run(suite)








