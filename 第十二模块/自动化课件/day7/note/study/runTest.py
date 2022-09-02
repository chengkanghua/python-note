import unittest
from case_set import CaseSet

class MyCase(unittest.TestCase):


    def runTest(self):
        if CaseSet().get_status_code() == 200:
            print('断言成功')
        else:

            print('断言失败')

class MyCase2(unittest.TestCase):
    def aaa(self):
        title = CaseSet().get_text_data()
        print("title", title)
        if CaseSet().get_text_data() == "百度一下":
            print('断言成功')
        else:

            print('断言失败')


if __name__ == '__main__':
    # case = MyCase()
    # case.run()
    case2 = MyCase2(methodName='aaa')
    case2.run()




import unittest
import requests

class MyCase(unittest.TestCase):

    def setUp(self):
        self.code = requests.get("https://www.baidu.com").status_code

    def tearDown(self):
        print("用例执行之后")

    def runTest(self):
        if self.code == 200:
            print('断言成功')
        else:
            print('断言失败')

if __name__ == '__main__':
    MyCase().run()










