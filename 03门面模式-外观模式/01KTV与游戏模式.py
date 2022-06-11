class Light:
    def on(self):
        print('light on')

    def off(self):
        print('light off')


class Mircophone:
    def on(self):
        print('microphone on')

    def off(self):
        print('microphone off')


class DVDPlayer():
    def on(self):
        print('dvdplayer on')

    def off(self):
        print('dvdplayer off')


class Game():
    def on(self):
        print('game on')

    def off(self):
        print('game off')


class Facade:
    def __init__(self):
        self.light = Light()
        self.microphone = Mircophone()
        self.dvd = DVDPlayer()
        self.game = Game()

    def runKTV(self):
        self.dvd.on()
        self.light.off()
        self.microphone.on()

    def runGame(self):
        self.dvd.on()
        self.game.on()


if __name__ == '__main__':
    Facade().runKTV()
    Facade().runGame()
