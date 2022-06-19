from abc import ABCMeta, abstractmethod

"""
在代理模式（Proxy Pattern）中，一个类代表另一个类的功能。这种类型的设计模式属于结构型模式。

在代理模式中，我们创建具有现有对象的对象，以便向外界提供功能接口。

1、Windows 里面的快捷方式。 
2、猪八戒去找高翠兰结果是孙悟空变的，可以这样理解：
把高翠兰的外貌抽象出来，高翠兰本人和孙悟空都实现了这个接口，猪八戒访问高翠兰的时候看不出来这个是孙悟空，
所以说孙悟空是高翠兰代理类。 
3、买火车票不一定在火车站买，也可以去代售点。
 4、一张支票或银行存单是账户中资金的代理。支票在市场交易中用来代替现金，
 并提供对签发人账号上资金的控制。 5、spring aop。
"""


class Image(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.loadFromDisk(filename)

    def display(self):
        print("Displaying " + self.filename)

    def loadFromDisk(self, filename):
        print("Loading " + filename)


class ProxyImage(Image):
    def __init__(self, realimage):
        self.realimage = realimage

    def other_process(self, realimage):
        print("other process")

    def display(self):
        self.other_process(self.realimage)
        self.realimage.display()


if __name__ == '__main__':
    proxyimage = ProxyImage(RealImage("a.png"))
    proxyimage.display()
