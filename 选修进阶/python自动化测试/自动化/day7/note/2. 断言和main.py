

import unittest
import requests

class MyCase(unittest.TestCase):

    def setUp(self):

        self.code = requests.get("https://www.baidu.com").status_code
        print("用力执行之前", self.code)
    def tearDown(self):
        print("用例执行之后")

    def test_case(self):
        # print(1111111111111)
        self.assertEqual(self.code, 201, msg="实际值：{}   预期值 {}".format(self.code, 201))   # 实际值，预期值，错误描述

    def test_case_02(self):
        """ 第二个测试用例  """
        print(self._testMethodDoc, self._testMethodName)


        self.assertTrue(1)



if __name__ == '__main__':
    unittest.main()

