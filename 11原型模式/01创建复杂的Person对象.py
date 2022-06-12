import copy
from collections import OrderedDict

"""
原型模式（Prototype Pattern）是用于创建重复的对象，同时又能保证性能。
这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

这种模式是实现了一个原型接口，该接口用于创建当前对象的克隆。
当直接创建对象的代价比较大时，则采用这种模式。例如，一个对象需要在一个高代价的数据库操作之后被创建。
我们可以缓存该对象，在下一个请求时返回它的克隆，在需要的时候更新数据库，以此来减少数据库调用。
"""


# 定义一个人的类，每次调用init创建对象很复杂，能不能简单些，用之前创建好的对象clone一个
class Person():
    def __init__(self, name, age, high, sex, **info):
        self.name = name
        self.age = age
        self.high = high
        self.sex = sex
        # 可以为实例添加其他额外属性，但必须是key:value格式的属性
        self.__dict__.update(info)

    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        info = []
        # OrderedDict 是 collections 提供的一种数据结构， 它提供了有序的dict结构。
        order_dict = OrderedDict(self.__dict__.items())
        for i in order_dict.keys():
            info.append('{}:{}'.format(i, order_dict[i]))
            info.append('\n')
        return ''.join(info)


# 定义原型类
class Prototype:
    def __init__(self):
        self.objects = dict()  # 定义原型对象字典表

    # 在原型字典表中注册原型对象
    def register(self, id, obj):
        self.objects[id] = obj

    # 在原型字典表中删除原型对象
    def destory(self, id):
        del self.objects[id]

    # 根据 id 在原型字典表中查找原型对象并克隆
    def clone(self, id, **atter):
        obj1 = self.objects.get(id)
        print(obj1)
        if not obj1:
            raise ValueError('Incorrect object id: {}'.format(id))
        obj2 = copy.deepcopy(obj1)
        obj2.__dict__.update(atter)
        return obj2


if __name__ == '__main__':
    tony = Person('tony', 34, 170, 'man', job='tester', birthday='2000-01-01', hobby='catch fish')
    print(tony)

    prototype = Prototype()
    prototype.register(1001, tony)
    tom = prototype.clone(1001, name='tom', age='19', birthday='2010-02-02')
    print(tom)
    # 输出两个Person对象是否是相同的id值
    print("id tony : {} != id tom : {}".format(id(tony), id(tom)))
