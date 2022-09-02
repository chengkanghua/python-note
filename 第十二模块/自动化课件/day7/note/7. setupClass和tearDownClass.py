


import unittest

class MyCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('所有用例执行之前')

    @classmethod
    def tearDownClass(cls):
        print('所有用例执行之后')

    def setUp(self):
        print('{}执行之前'.format(self._testMethodName))
    def tearDown(self):
        print('{}执行之后'.format(self._testMethodName))

    def test_is_upper(self):
        self.assertTrue('FOO'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())



if __name__ == '__main__':
    unittest.main(verbosity=2)


