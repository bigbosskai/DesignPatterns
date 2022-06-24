from abc import ABCMeta, abstractmethod

"""
在策略模式（Strategy Pattern）中，一个类的行为或其算法可以在运行时更改。这种类型的设计模式属于行为型模式。

在策略模式中，我们创建表示各种策略的对象和一个行为随着策略对象改变而改变的 context 对象。策略对象改变 context 对象的执行算法。
使用场景： 
1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。 
2、一个系统需要动态地在几种算法中选择一种。 
3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现
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
