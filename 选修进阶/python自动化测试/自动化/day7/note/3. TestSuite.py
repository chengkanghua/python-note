


# ----------------- addTest --------------------

# import unittest
#
# class MyCase(unittest.TestCase):
#
#     def test_is_upper(self):
#         self.assertTrue('Foo'.isupper())
#
#     def test_is_lower(self):
#         self.assertTrue('foo'.islower())
#
#
# if __name__ == '__main__':
#     case_01 = MyCase(methodName='test_is_upper')
#     case_02 = MyCase(methodName='test_is_lower')
#     # 创建suite
#     suite = unittest.TestSuite()
#     # 将用例添加到盒子中
#     suite.addTest(case_01)
#     suite.addTest(case_02)
#     # 使用执行器执行suite中的测试用例
#     runner = unittest.TextTestRunner()
#     runner.run(suite)



# ----------------- addTests --------------------
# import unittest
#
# class MyCase(unittest.TestCase):
#
#     def test_is_upper(self):
#         self.assertTrue('Foo'.isupper())
#
#     def test_is_lower(self):
#         self.assertTrue('foo'.islower())
#
#
# if __name__ == '__main__':
#     case_01 = MyCase(methodName='test_is_upper')
#     case_02 = MyCase(methodName='test_is_lower')
#     # 创建suite
#     suite = unittest.TestSuite()
#     # 将用例添加到盒子中
#     suite.addTests([case_01, case_02])
#     # 使用执行器执行suite中的测试用例
#     runner = unittest.TextTestRunner()
#     runner.run(suite)




# ----------------- map --------------------
import unittest

class MyCase(unittest.TestCase):

    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())


if __name__ == '__main__':
    # case_01 = MyCase(methodName='test_is_upper')
    # case_02 = MyCase(methodName='test_is_lower')

    case_obj = map(MyCase, ['test_is_upper', 'test_is_lower'])
    # print(case_obj, list(case_obj))
    # 创建suite
    suite = unittest.TestSuite()
    # 将用例添加到盒子中
    suite.addTests(case_obj)
    # 返suite中测试用例的个数
    print(11111111, suite.countTestCases())

    # 使用执行器执行suite中的测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)













