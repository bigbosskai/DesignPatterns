from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News:", self.__latestNews


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publiser = publisher
        self.publiser.attach(self)

    def update(self):
        print(type(self).__name__, self.publiser.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publiser = publisher
        self.publiser.attach(self)

    def update(self):
        print(type(self).__name__, self.publiser.getNews())


if __name__ == '__main__':
    publisher = NewsPublisher()
    sms = SMSSubscriber(publisher)
    email = EmailSubscriber(publisher)
    publisher.addNews("fuck you")
    publisher.notifySubscribers()

    publisher.addNews('love you')
    publisher.notifySubscribers()
