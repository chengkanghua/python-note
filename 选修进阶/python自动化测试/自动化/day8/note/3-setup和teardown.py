import pytest



def setup_module():
    print("模块级别的 setup_module")


def teardown_module():
    print("模块级别的 teardown_module")


def setup_function():
    print("在函数执行前执行我")

def teardown_function():
    print("在函数执行后执行我")

def test_case_01():

    assert 1

def test_case_02():

    assert 1


class TestCase(object):

    def setup_class(self):
        print("在类中，所有用例执行 前 执行我")

    def teardown_class(self):
        print("在类中，所有用例执行 后 执行我")

    def setup_method(self):
        print("类中方法级别， 在用例 前 执行我")

    def teardown_method(self):
        print("类中方法级别， 在用例 后 执行我")

    def test_case_03(self):
        assert 1

    def test_case_04(self):
        assert 1


if __name__ == '__main__':
    pytest.main(['-v', '-s', '3-setup和teardown.py'])



