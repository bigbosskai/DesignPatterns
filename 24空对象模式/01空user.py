from abc import ABCMeta, abstractmethod

"""
在空对象模式（Null Object Pattern）中，一个空对象取代 NULL 对象实例的检查。Null 对象不是检查空值，
而是反应一个不做任何动作的关系。这样的 Null 对象也可以在数据不可用的时候提供默认的行为。

在空对象模式中，我们创建一个指定各种要执行的操作的抽象类和扩展该类的实体类，
还创建一个未对该类做任何实现的空对象类，该空对象类将无缝地使用在需要检查空值的地方。
"""


class AbstractCustomer(metaclass=ABCMeta):
    name = ""

    @abstractmethod
    def isNil(self):
        pass

    @abstractmethod
    def getName(self):
        pass


# 创建扩展了AbstractCustomer的实体类
class RealCustomer(AbstractCustomer):
    def __init__(self, inName):
        self.name = inName

    def getName(self):
        return self.name

    def isNil(self):
        return False


class NullCustomer(AbstractCustomer):
    def getName(self):
        return "Not Available in Customer Database"

    def isNil(self):
        return True


# 创建CustomerFactory类
class CustomerFactory():
    names = ["Rob", "Joe", "Julie"]

    @staticmethod
    def getCustomer(inName):
        for aName in CustomerFactory.names:
            if aName.upper() == inName.upper():
                return RealCustomer(inName)
        return NullCustomer()  # 调用输出


if __name__ == '__main__':
    customer1 = CustomerFactory.getCustomer("Rob")
    customer2 = CustomerFactory.getCustomer("Bob")
    customer3 = CustomerFactory.getCustomer("Julie")
    customer4 = CustomerFactory.getCustomer("Laura")
    print("Customers")
    print(customer1.getName())
    print(customer2.getName())
    print(customer3.getName())
    print(customer4.getName())
