from abc import ABCMeta, abstractmethod


class AbstractHero(metaclass=ABCMeta):
    # After receiving the notification, execute update
    @abstractmethod
    def update(self):
        pass


class HeroA(AbstractHero):
    def __init__(self):
        print('heroA')

    def update(self):
        print('heaoA stop')


class HeroB(AbstractHero):
    def __init__(self):
        print('heroB')

    def update(self):
        print('heaoB stop')


class HeroC(AbstractHero):
    def __init__(self):
        print('heroC')

    def update(self):
        print('heaoC stop')


class AbstractBoss(metaclass=ABCMeta):
    @abstractmethod
    def addHero(self, hero):
        pass

    @abstractmethod
    def deleteHero(self, hero):
        pass

    @abstractmethod
    def notify(self):
        pass


class BossA(AbstractBoss):
    def __init__(self):
        self.heroes = []

    def addHero(self, hero):
        self.heroes.append(hero)

    def deleteHero(self, hero):
        self.heroes.remove(hero)

    def notify(self):
        for h in self.heroes:
            h.update()


if __name__ == '__main__':
    b = BossA()
    ha = HeroA()
    hb = HeroB()
    hc = HeroC()
    b.addHero(ha)
    b.addHero(hb)
    b.addHero(hc)
    b.deleteHero(hb)
    b.notify()
