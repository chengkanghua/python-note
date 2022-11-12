


import pytest





@pytest.mark.skip(reason='无条件跳过')
def test_case_01():
    assert 1


@pytest.mark.skipif(condition=1 < 2, reason="condition条件为真时跳过用例")
def test_case_02():

    assert 1





