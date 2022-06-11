from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def doAction(self, context):
        pass


class StartState(State):
    def doAction(self, context):
        print('player is in start state')
        context.setState(self)


class StopState(State):
    def doAction(self, context):
        print('player is in stop state')
        context.setState(self)


class Context:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def __str__(self):
        return type(self.state).__name__


if __name__ == '__main__':
    context = Context()
    sstart = StartState()
    sstop = StopState()
    sstart.doAction(context)
    print(context)
    sstop.doAction(context)
    print(context)
