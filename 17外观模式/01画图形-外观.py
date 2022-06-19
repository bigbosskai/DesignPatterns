from abc import ABCMeta, abstractmethod

"""

外观模式（Facade Pattern）隐藏系统的复杂性，并向客户端提供了一个客户端可以访问系统的接口。
这种类型的设计模式属于结构型模式，它向现有的系统添加一个接口，来隐藏系统的复杂性。

这种模式涉及到一个单一的类，该类提供了客户端请求的简化方法和对现有系统类方法的委托调用。

想想电视机的盒子，内部我们看不见，只需要通过电视机上面的开关、音量调节按钮就可以控制了
"""


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")


class Circle(Shape):
    def draw(self):
        print("Shape: Circle")


class Square(Shape):
    def draw(self):
        print("Shape: Square")


class ShapeMaker:
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()

    def drawCircle(self):
        self.circle.draw()

    def drawSquare(self):
        self.square.draw()

    def drawRectangle(self):
        self.rectangle.draw()


if __name__ == '__main__':
    ShapeMaker().drawSquare()
    ShapeMaker().drawCircle()
