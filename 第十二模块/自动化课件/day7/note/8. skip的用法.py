

import unittest


class MyCase(unittest.TestCase):


    def test_case_01(self):
        self.assertTrue(1)


    @unittest.skip(reason='无条件跳过')
    def test_case_02(self):
        self.assertTrue("")

    @unittest.skipIf(condition=3 < 2, reason='有条件跳过')
    def test_case_03(self):
        self.assertTrue(0)


if __name__ == '__main__':
    unittest.main(verbosity=2)