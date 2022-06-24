from abc import ABCMeta, abstractmethod


class Subject:
    def __init__(self):
        self.__observers = []
        self.state = None

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for obs in self.__observers:
            obs.update(self, *args, **kwargs)

    def setState(self, state):
        self.state = state
        self.notifyAll()

    def getState(self):
        return self.state


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class BinaryObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def update(self, *args, **kwargs):
        print("binary string: {}".format(bin(self.subject.getState())))


class OctalObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def update(self, *args, **kwargs):
        print("octal string: {}".format(oct(self.subject.getState())))


class HexaObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def update(self, *args, **kwargs):
        print("hexa string: {}".format(hex(self.subject.getState())))


if __name__ == '__main__':
    subject = Subject()
    BinaryObserver(subject)
    OctalObserver(subject)
    HexaObserver(subject)

    subject.setState(100)
