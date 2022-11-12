

import pytest




def test_run_01():
    print('第一个用例')
    assert 1


def test_run_02():
    print('第二个用例')
    assert 0

class TestCase(object):

    def test_case_01(self):
        print("第三个用例")
        assert 1

    def test_case_02(self):
        print("第三个用例")
        assert 1



if __name__ == '__main__':
    pytest.main(['-s','2-pytest简单使用.py'])

    '''
    ModuleNotFoundError: No module named '2'
    '''

