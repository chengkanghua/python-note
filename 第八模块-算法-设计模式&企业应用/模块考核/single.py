import threading

class Singletion:
    instance = None
    lock = threading.RLock()
    def __init__(self):
        self.name = 'eric'

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
        return cls.instance

obj1 = Singletion()
obj2 = Singletion()
print(obj1 is obj2)

