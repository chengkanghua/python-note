class Person(object):
    title = "北京"
    def __init__(self, name, wx):
        self.name = name
        self.wx = wx
    def show(self):
        message = "姓名{}，微信：{}".format(self.name, self.wx)
        return message
    @property
    def message(self):
        return 666
    @staticmethod
    def something():
        return 999
obj = Person("武沛齐", "wupeiqi666")

print(getattr(obj, 'wx')) #wupeiqi666
print(getattr(obj, 'message')) # 666
print(getattr(obj, 'show')()) # 姓名武沛齐，微信：wupeiqi666
print(getattr(obj, 'something')()) #999