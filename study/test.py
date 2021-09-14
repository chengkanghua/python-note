# 请基于`__new__` 实现一个单例类（加锁）。
import threading


class Singleton(object):
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = super().__new__(cls)
        return cls.instance


t1 = Singleton('aaa')
t2 = Singleton('bbbb')
print(t1 is t2)
