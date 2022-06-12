from abc import ABCMeta, abstractmethod


class AbstractSystem(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class System(AbstractSystem):
    def run(self):
        print('系统真的开启')


# There is a System instance inside
class ProxySystem(AbstractSystem):
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        self.system = System()

    def run(self):
        if self.username == 'adam' and self.passwd == '123':
            self.system.run()
        else:
            print('passwd error')


if __name__ == '__main__':
    system = ProxySystem('adam', '123')
    system.run()
