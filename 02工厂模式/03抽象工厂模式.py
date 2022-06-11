from abc import ABCMeta, abstractmethod


class AbstractApple(metaclass=ABCMeta):
    @abstractmethod
    def show_name(self):
        pass


class AbstractBanana(metaclass=ABCMeta):
    @abstractmethod
    def show_name(self):
        pass


class AbstractPear(metaclass=ABCMeta):
    @abstractmethod
    def show_name(self):
        pass


class ChinaApple(AbstractApple):
    def show_name(self):
        print('chinea apple')


class ChinaBanana(AbstractBanana):
    def show_name(self):
        print('chinea banana')


class ChinaPear(AbstractPear):
    def show_name(self):
        print('chinea pear')


class USAApple(AbstractApple):
    def show_name(self):
        print('usa apple')


class USABanana(AbstractBanana):
    def show_name(self):
        print('usa banana')


class USAPear(AbstractPear):
    def show_name(self):
        print('usa pear')


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def createApple(self):
        pass

    @abstractmethod
    def createBanana(self):
        pass

    @abstractmethod
    def createPear(self):
        pass


class ChinaFactorary(AbstractFactory):
    def createApple(self):
        return ChinaApple()

    def createPear(self):
        return ChinaPear()

    def createBanana(self):
        return ChinaBanana()


class USAFactorary(AbstractFactory):
    def createApple(self):
        return USAApple()

    def createPear(self):
        return USAPear()

    def createBanana(self):
        return USABanana()


if __name__ == '__main__':
    eval('ChinaFactorary')().createApple().show_name()
    eval('ChinaFactorary')().createPear().show_name()
    eval('ChinaFactorary')().createBanana().show_name()

    eval('USAFactorary')().createApple().show_name()
    eval('USAFactorary')().createPear().show_name()
    eval('USAFactorary')().createBanana().show_name()
