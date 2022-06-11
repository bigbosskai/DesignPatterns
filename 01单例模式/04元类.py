class MyInt(type):
    def __call__(self, *args, **kwargs):
        print('*** here is my int ***', args)
        return type.__call__(self, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4, 5)
"""
*** here is my int *** (4, 5)
"""


# 利用元类实现单例
class MetaSingleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            # 下面也就是调用Logger的new和init方法
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)
"""
<__main__.Logger object at 0x104f5ed30>
<__main__.Logger object at 0x104f5ed30>

"""


class Mymeta(type):
    def __call__(self, *args, **kwargs):
        print(args) # 1
        obj = self.__new__(self)
        self.__init__(obj, *args, **kwargs) # 2 调用3
        return obj #返回对象

class Teacher(metaclass=Mymeta):
    def __init__(self, name, age=17): # 3
        self.name = name
        self.age = age

t1 = Teacher("lili")
print(t1)

