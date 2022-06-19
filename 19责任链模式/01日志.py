from abc import ABCMeta, abstractmethod

"""
顾名思义，责任链模式（Chain of Responsibility Pattern）为请求创建了一个接收者对象的链。
这种模式给予请求的类型，对请求的发送者和接收者进行解耦。
这种类型的设计模式属于行为型模式。

在这种模式中，通常每个接收者都包含对另一个接收者的引用。
如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，
依此类推。


1、有多个对象可以处理同一个请求，具体哪个对象处理该请求由运行时刻自动确定。
2、在不明确指定接收者的情况下，向多个对象中的一个提交一个请求。
3、可动态指定一组对象处理请求。
"""


class AbstractLogger(metaclass=ABCMeta):
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def setNextLogger(self, next_logger):
        self.next_logger = next_logger

    @abstractmethod
    def write(self, msg):
        pass

    def log_msg(self, level, msg):
        if self.level <= level:
            self.write(msg)
        if self.next_logger is not None:
            self.next_logger.log_msg(level, msg)


class ConsoleLogger(AbstractLogger):
    def __init__(self, level):
        super(ConsoleLogger, self).__init__(level)

    def write(self, msg):
        print("standard console: %s" % msg)


class ErrorLogger(AbstractLogger):
    def __init__(self, level):
        super(ErrorLogger, self).__init__(level)

    def write(self, msg):
        print("error console: %s" % msg)


class FileLogger(AbstractLogger):
    def __init__(self, level):
        super(FileLogger, self).__init__(level)

    def write(self, msg):
        print("file logger: %s" % msg)


def getChainOfLoggers():
    errorLogger = ErrorLogger(AbstractLogger.ERROR)
    fileLogger = FileLogger(AbstractLogger.DEBUG)
    consoleLogger = ConsoleLogger(AbstractLogger.INFO)

    errorLogger.setNextLogger(fileLogger)
    fileLogger.setNextLogger(consoleLogger)

    return errorLogger


if __name__ == '__main__':
    loggerChain = getChainOfLoggers()
    loggerChain.log_msg(AbstractLogger.INFO, "This is an info information.")
    loggerChain.log_msg(AbstractLogger.DEBUG, "This is an debug information.")
    loggerChain.log_msg(AbstractLogger.ERROR, "This is an error information.")
