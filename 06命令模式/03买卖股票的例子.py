from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print('you will buy stocks')

    def sell(self):
        print('you will sell stocks')


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    stock = StockTrade()
    buystock = BuyStockOrder(stock)
    sellstock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buystock)
    agent.placeOrder(sellstock)
