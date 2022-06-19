from abc import ABCMeta, abstractmethod
"""
命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。
请求以命令的形式包裹在对象中，并传给调用对象。调用对象寻找可以处理该命令的合适的对象，
并把该命令传给相应的对象，该对象执行命令。

认为是命令的地方都可以使用命令模式，比如： 1、GUI 中每一个按钮都是一条命令。 2、模拟 CMD。
"""

class HandleClientProtocol:
    # Several commands to be executed are encapsulated in protocols
    def addMoney(self):
        print('add money')

    def addDiamond(self):
        print("add diamond")

    def addEquipment(self):
        print('add equipment')

    def addLevel(self):
        print('add level')


class AbstractCommand(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class AddMoneyCommand(AbstractCommand):
    def __init__(self, protocal):
        self.protocal = protocal

    def handle(self):
        self.protocal.addMoney()


class AddDiamondCommand(AbstractCommand):
    def __init__(self, protocal):
        self.protocal = protocal

    def handle(self):
        self.protocal.addDiamond()


class AddEquipmentCommand(AbstractCommand):
    def __init__(self, protocal):
        self.protocal = protocal

    def handle(self):
        self.protocal.addEquipment()


class Server:
    def __init__(self):
        self.tasks = []

    def addRequest(self, command):
        self.tasks.append(command)

    def startHandle(self):
        while len(self.tasks) > 0:
            self.tasks[-1].handle()
            self.tasks.pop()


if __name__ == '__main__':
    s = Server()
    pro = HandleClientProtocol()
    s.addRequest(AddMoneyCommand(pro))
    s.addRequest(AddEquipmentCommand(pro))
    s.startHandle()

    s.addRequest(AddMoneyCommand(pro))
    s.addRequest(AddEquipmentCommand(pro))
    s.addRequest(AddDiamondCommand(pro))
    s.startHandle()
