class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


b = Borg()
b1 = Borg()
print(b)
print(b1)
b.x = 4
print(b.__dict__)
print(b1.__dict__)
"""
两个是不同的对象但是还是共享了内容
<__main__.Borg object at 0x100d78fd0>
<__main__.Borg object at 0x100d78df0>
{'1': '2', 'x': 4}
{'1': '2', 'x': 4}
"""


# 除此之外还可以通过new来实现
class BorgNew(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(BorgNew, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
