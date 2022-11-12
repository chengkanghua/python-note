
import pytest



def test_case_07():
    assert 1


@pytest.mark.run(order=2)
def test_case_02():
    assert 1
@pytest.mark.run(order=1)
def test_case_01():
    assert 1
@pytest.mark.run(order=3)
def test_case_03():
    assert 0

class TestCase(object):

    def test_case_06(self):
        assert 1

    def test_case_05(self):
        assert 1

    @pytest.mark.run(order=4)
    def test_case_04(self):
        assert 0

