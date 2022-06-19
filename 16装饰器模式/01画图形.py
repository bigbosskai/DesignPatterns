from abc import ABCMeta, abstractmethod

"""
装饰器模式（Decorator Pattern）允许向一个现有的对象添加新的功能，
同时又不改变其结构。这种类型的设计模式属于结构型模式，
它是作为现有的类的一个包装。

这种模式创建了一个装饰类，用来包装原有的类，并在保持类方法签名完整性的前提下，
提供了额外的功能。

我们通过下面的实例来演示装饰器模式的用法。其中，我们将把一个形状装饰上不同的颜色，
同时又不改变形状类。

1、孙悟空有 72 变，当他变成"庙宇"后，他的根本还是一只猴子，
但是他又有了庙宇的功能。 2、不论一幅画有没有画框都可以挂在墙上，
但是通常都是有画框的，并且实际上是画框被挂在墙上。在挂在墙上之前，
画可以被蒙上玻璃，装到框子里；这时画、玻璃和画框形成了一个物体。

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


class ShapeDecorator(Shape):
    def __init__(self, decoratedshape):
        self.decoratedshape = decoratedshape

    def draw(self):
        self.decoratedshape.draw()


class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decoratedshape):
        super(RedShapeDecorator, self).__init__(decoratedshape)

    def draw(self):
        self.decoratedshape.draw()
        self.setRedBorder(self.decoratedshape)

    def setRedBorder(self, decoratedshape):
        print("Border Color: Red")


if __name__ == "__main__":
    circle = Circle()
    redcircle = RedShapeDecorator(circle)
    redrectangle = RedShapeDecorator(Rectangle())

    circle.draw()
    redcircle.draw()
    redrectangle.draw()
