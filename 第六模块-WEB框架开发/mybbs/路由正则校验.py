#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/5/23

import re


r1 = re.compile(r'(\w+)/(tag|category|archive)/(.+)/$')
r2 = re.compile(r'(\w+)/$')


s1 = "egon/tag/python/"
s2 = "egon/tag/2016-10/"
s3 = "egon/"

ret1 = r1.match(s1)
print(ret1)
ret2 = r1.match(s2)
print(ret2)
ret3 = r1.match(s3)
print(ret3)

print("=" * 120)

ret1 = r2.match(s1)
print(ret1)
ret2 = r2.match(s2)
print(ret2)
ret3 = r2.match(s3)
print(ret3)
