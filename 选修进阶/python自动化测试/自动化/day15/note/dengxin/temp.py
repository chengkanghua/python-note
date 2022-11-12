# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 8:25
# @Author  : 张开
# File      : temp.py



import unittest
from HTMLTestRunner import HTMLTestRunner


from deepdiff import DeepDiff



d1 = {'code': '0', 'message': 'success',
              'data': {'skuId': 1, 'skuName': 'ptest-1', 'price': '922', 'stock': 74, 'brand': 'testfan'}}
d2 = {"code": "0"}
d3 = {"code": 0}




class My(unittest.TestCase):

    def test_case_01(self):

        self.assertEqual(DeepDiff(d1, d3).get('type_changes', None), None)
    def test_case_02(self):
        self.assertEqual(DeepDiff(d1, d2).get('type_changes', None), None)

    def test_case_03(self):
        self.assertEqual( 1,1)

if __name__ == '__main__':
    f = open('a.html', 'wb')
    suite = unittest.makeSuite(testCaseClass=My, prefix='test')
    # print(suite.countTestCases())
    obj = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='a',
        description='bbbb',
    )
    result = obj.run(suite)
    # print(111111, obj.__dict__['result'])
    # print(111111, result.__dict__['result'])


    # print(1111111, result.__dict__)
    d = {'pass': 0, "failed":0, "total": 0, "errors": 0}
    for i in result.__dict__['result']:
        # print(i[0], i[1].__dict__['_testMethodName'])
        if i[0]:
            d["failed"] += 1
        else:
            d['pass'] += 1
        d['total'] += 1
    d['errors'] = result.__dict__['errors'].__len__()
    print(d)
    f.close()
