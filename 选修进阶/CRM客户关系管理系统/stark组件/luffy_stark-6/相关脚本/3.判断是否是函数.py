#!/usr/bin/env python
# -*- coding:utf-8 -*-
from types import FunctionType


def func(arg):
    pass

# 如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。。
print(isinstance('sadf', FunctionType))
print(isinstance('func', str)) # true
print(isinstance(func,FunctionType)) # true

#
