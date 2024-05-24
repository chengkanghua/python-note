import time
import threading


class Foo(object):
    instance = None
    lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = super().__new__(cls)
            return cls.instance


def task():
    obj1 = Foo()  # 创建了对象
    print(obj1)  # 用的都是第一次创建的对象


for i in range(50):
    t = threading.Thread(target=task)
    t.start()

# 。。。。。

v1 = Foo()
