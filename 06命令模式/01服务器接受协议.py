from abc import ABCMeta, abstractmethod


class HandleClientProtocol:
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
