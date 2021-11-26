#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    pass


# 实例化了一个Foo类的对象（实例）
obj1 = Foo()
print(obj1)  # <__main__.Foo object at 0x1021787f0>
obj1.name = '武沛齐'


# 实例化了一个Foo类的对象（实例）
obj2 = Foo()
print(obj2)  # <__main__.Foo object at 0x1021787b8>
#print(obj2.name)
