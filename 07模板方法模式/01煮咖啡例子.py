from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    @abstractmethod
    def boildWater(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def pourInCup(self):
        pass

    @abstractmethod
    def addSomething(self):
        pass

    def make(self):
        self.boildWater()
        self.brew()
        self.pourInCup()
        self.addSomething()


class Tea(Template):
    def boildWater(self):
        print('烧开水')

    def brew(self):
        print('冲泡茶叶')

    def pourInCup(self):
        print('茶叶到入杯子中')

    def addSomething(self):
        print('加入柠檬')


class Coffee(Template):
    def boildWater(self):
        print('烧农夫山泉')

    def brew(self):
        print('冲泡咖啡')

    def pourInCup(self):
        print('咖啡到入杯子中')

    def addSomething(self):
        print('加入牛奶')


if __name__ == '__main__':
    Tea().make()
    Coffee().make()
