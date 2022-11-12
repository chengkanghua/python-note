


import pytest





@pytest.mark.xfail()
def test_case_01():
    assert 1


@pytest.mark.xfail()
def test_case_02():
    assert 0


def test_case_03():
    assert 1

def test_case_04():
    assert 0





# @pytest.mark.skipif(condition=1 < 2, reason="condition条件为真时跳过用例")
# def test_case_02():
#
#     assert 1





