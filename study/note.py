import os
# print(os.getcwd())  # 打印当前文件运行时工作目录

# yield 1  和 1 = yield 区别？
# nolocal 和 gloab 区别

# 深浅拷贝区别
# 针对 可变类型来说的，  深拷贝是拷贝可变类型数据， 浅拷贝不会(拷贝的是内存地址）

# staticmethod 静态方法里不可以调用累的其他方法     self.add() 报错

'''
class Foo(object):
    country = '中国' #类变量，属于类，可以被所有对象共享，一般用于给对象提供公共数据（类似于全局变量）。
    __city = '景德镇' # __开头 私有，只有在类的内部才可以调用改成员
    def __init__(self, name, age,sex): # name age 实例变量，属于对象，每个对象中各自维护自己的数据。
        self.name = name
        self.age = age
        self.__sex = sex
    def __f0(self):
        print('__f0')
    def f1(self):
        # print("绑定方法", self.name)
        print(self.__city,self.__sex)
        self.__f0()
        self.f2()
        self.f3()
    @classmethod
    def f2(cls):
        # print("类方法", cls)
        print(cls.__city)
        print(cls.country)
        cls.f3()            #可以访问静态方法
        # cls.__f0()        #类方法访问不了私有方法__f0()
        # cls.f1()          #类方法访问不了绑定方法
        # print(cls.age)    #类方法访问不了init初始化的变量
        # print(cls.__sex)  #类方法不能访问init初始化的私有成员
    @staticmethod
    def f3():               # 静态方法没法访问类中其他方法和变量
        print("静态方法")

obj = Foo('alex',18,'男')
Foo.f1(obj)  #类调用绑定方法需要吧对象作为参数
# Foo.f2()  # cls就是当前调用这个方法的类。（类）
# Foo.f3() # 类执行执行方法（类）

# obj = Foo("武沛齐", 20,'男')
# obj.f1()  # Foo.f1(obj)
# obj.f2()
# obj.f3()
'''













