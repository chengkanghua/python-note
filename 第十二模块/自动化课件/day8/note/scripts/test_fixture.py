


import pytest


@pytest.fixture()
def login():
    print("登录成功")


def test_index(login):  # 该用例执行之前要登录
    print("index page")
    assert 1




@pytest.fixture()
def db():
    print("connect db。。。")

    yield

    print('close db .....')

def test_index(db):  # 该用例执行之前要登录
    print("index page")
    assert 1



















