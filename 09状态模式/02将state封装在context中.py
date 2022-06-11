from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class StartState(State):
    def handle(self):
        print('player is in start state')


class StopState(State):
    def handle(self):
        print('player is in stop state')


class Context(State):
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def handle(self):
        self.state.handle()


if __name__ == '__main__':
    context = Context()
    sstart = StartState()
    sstop = StopState()
    context.setState(sstop)
    context.handle()
