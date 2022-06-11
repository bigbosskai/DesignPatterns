from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('wang wang wang')


class Cat(Animal):
    def do_say(self):
        print('miao miao miao')


class Factory(object):
    def create(self, object_type):
        return eval(object_type)()


if __name__ == '__main__':
    a = Factory().create('Cat')
    a.do_say()
    # a = Animal() # 不能创建对象的
