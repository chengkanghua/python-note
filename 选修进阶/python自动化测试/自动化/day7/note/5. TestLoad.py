



import unittest

from scripts import ff_case


class MyCase(unittest.TestCase):

    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())

    def foo_is_instance(self):
        self.assertIsInstance([1, 2], list)


if __name__ == '__main__':

    from scripts import ff_case
    # suite = unittest.makeSuite(MyCase)

    # suite = unittest.TestLoader().loadTestsFromModule(ff_case)
    # suite = unittest.TestLoader().loadTestsFromName(
    #     name="MyTestCase.test_case_02",   # 类.用例名称
    #     module=ff_case   # 模块名
    # )
    suite = unittest.TestLoader().loadTestsFromNames(
        names=[
            "MyTestCase.test_case_01",
            "MyTestCase.test_case_02",
        ],
        module=ff_case
    )

    unittest.TextTestRunner(
        verbosity=2
    ).run(suite)

    # 发现指定目录中的所有合法的脚本中的合法的测试用例
    # import os
    # SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
    # index_dir = os.path.join(SCRIPTS_DIR, 'index')
    # suite = unittest.TestLoader().discover(
    #     top_level_dir=SCRIPTS_DIR,
    #     start_dir= index_dir,
    #     pattern='ff_*'
    # )
    # unittest.TextTestRunner(
    #     verbosity=2
    # ).run(suite)












