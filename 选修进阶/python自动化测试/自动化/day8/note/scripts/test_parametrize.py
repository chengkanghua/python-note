

import requests
import pytest
import allure



url_list = [
    {'url': "https://www.baidu.com", "method": "get", "status": 200, "title": "百度"},
    {'url': "https://www.cnblogs.com/Neeo/articles/11832655.html", "method": "get", "status": 200, "title":"cnblogs"},
    {'url': "http://www.neeo.cc:6001/post", "method": "post", "status": 200, "title":"post接口"},
    {'url': "http://www.neeo.cc:6001/put", "method": "put", "status": 200, "title":"put接口"},
]


@pytest.mark.parametrize('item', url_list)
def test_case(item):

    allure.dynamic.title(item['title'])
    response = requests.request(method=item['method'], url=item['url'])
    # print(response.status_code,  item['status'])
    assert response.status_code == item['status']













# phone = [10086, 10010, 110]
# code = ['10086', '10010', '110']
#
#
# @pytest.mark.parametrize('item,code', zip(phone, code))
# def test_case(item, code):
#     print(111, item, code)
#     assert 1






# phone = [10086, 10010, 110]
# code = ['10086', '10010', '110']
#
#
# @pytest.mark.parametrize('item', phone)
# @pytest.mark.parametrize('code', code)
# def test_case(item, code):
#     print(111, item, code)
#     assert 1

# def test_case_01():
#     print(phone[0])
#     assert phone[0] == 10086

# def test_case_02():
#     print(phone[1])
#     assert phone[1] == 10010
#
# def test_case_03():
#     print(phone[2])
#     assert phone[2] == 110

