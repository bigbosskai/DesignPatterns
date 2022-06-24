from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def startPlay(self):
        pass

    @abstractmethod
    def endPlay(self):
        pass

    def play(self):
        self.initialize()

        self.startPlay()

        self.endPlay()


class Cricket(Game):

    def initialize(self):
        print("Cricket Game Initialized! Start playing.")

    def startPlay(self):
        print("Cricket Game Started. Enjoy the game!")

    def endPlay(self):
        print("Cricket Game Finished!")


class Football(Game):

    def initialize(self):
        print("Football Game Initialized! Start playing.")

    def startPlay(self):
        print("Football Game Started. Enjoy the game!")

    def endPlay(self):
        print("Football Game Finished!")


if __name__ == '__main__':
    Cricket().play()
    Football().play()
