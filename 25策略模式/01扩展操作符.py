from abc import ABCMeta, abstractmethod

"""
在策略模式（Strategy Pattern）中，一个类的行为或其算法可以在运行时更改。这种类型的设计模式属于行为型模式。

在策略模式中，我们创建表示各种策略的对象和一个行为随着策略对象改变而改变的 context 对象。策略对象改变 context 对象的执行算法。
"""


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def doOperation(self, a, b):
        pass


class AddOperation(Strategy):
    def doOperation(self, a, b):
        return a + b


class SubOperation(Strategy):
    def doOperation(self, a, b):
        return a - b


class MulOperation(Strategy):
    def doOperation(self, a, b):
        return a * b


class Context(Strategy):
    def __init__(self, oper):
        self.oper = oper

    def setOperation(self, oper):
        self.oper = oper

    def doOperation(self, a, b):
        return self.oper.doOperation(a, b)


if __name__ == '__main__':
    context = Context(AddOperation())
    print(context.doOperation(3, 5))

    context = Context(MulOperation())
    print(context.doOperation(3, 5))
