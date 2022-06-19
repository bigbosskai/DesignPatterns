from abc import ABCMeta, abstractmethod
import random

"""
享元模式（Flyweight Pattern）主要用于减少创建对象的数量，以减少内存占用和提高性能。
这种类型的设计模式属于结构型模式，它提供了减少对象数量从而改善应用所需的对象结构的方式。

享元模式尝试重用现有的同类对象，如果未找到匹配的对象，则创建新对象。我们将通过创建 
5 个对象来画出 20 个分布于不同位置的圆来演示这种模式。由于只有 5 种可用的颜色，
所以 color 属性被用来检查现有的 Circle 对象。

下面的例子共享颜色相同的对象
"""


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setRadius(self, radius):
        self.radius = radius


class ColorCircle(Circle):
    def __init__(self, color):
        super(ColorCircle, self).__init__(0, 0, 0)
        self.color = color

    def draw(self):
        print("{}\t{}\t{}\t{}".format(self.color, self.x, self.y, self.radius))


class ShapeFactory():
    circleMap = {}

    def __init__(self):
        pass

    @staticmethod
    def getCircle(color):
        circle = ShapeFactory.circleMap.get(color, None)
        if circle is None:
            circle = ColorCircle(color)
            ShapeFactory.circleMap[color] = circle
            print("Creating circle of color: %s" % color)
        return circle


def random_int():
    return int(random.random() * 100)


def random_color():
    return int(random.random() * 5)


if __name__ == '__main__':
    colors = ["Red", "Green", "Blue", "White", "Black"]
    for i in range(20):
        circle = ShapeFactory.getCircle(colors[random_color()])
        circle.setX(random_int())
        circle.setY(random_int())
        circle.setRadius(100)
        circle.draw()
