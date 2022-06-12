from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def packing(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Packing(metaclass=ABCMeta):
    # 对打包方式的抽象，提供盒子打包、瓶子打包两种打包方式
    @abstractmethod
    def pack(self):
        pass


class Bottle(Packing):
    def pack(self):
        return "瓶子打包方式"


class Wrapper(Packing):
    def pack(self):
        return "盒子打包方式"


class Burger(Item):
    # 汉堡包抽象类
    def packing(self):
        return Wrapper()


class ColdDrink(Item):
    # 饮料抽象类
    def packing(self):
        return Bottle()


class VegBurger(Burger):
    def price(self):
        return 25.0

    def name(self):
        return "veg burger"


class ChickenBurger(Burger):
    def price(self):
        return 50.0

    def name(self):
        return "chicken burger"


class Coke(ColdDrink):
    def price(self):
        return 12.5

    def name(self):
        return "coke"


class Pepsi(ColdDrink):
    def price(self):
        return 16.5

    def name(self):
        return "pepsi"


class Meal:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def getCost(self):
        cost = 0
        for i in self.items:
            cost += i.price()
        return cost

    def showItems(self):
        for i in self.items:
            print("{}\t{}\t{}".format(i.name(), i.packing().pack(), i.price()))


class MealBuilder:
    @staticmethod
    def prepareVegMeal():
        meal = Meal()
        meal.add(VegBurger())
        meal.add(Coke())
        return meal

    @staticmethod
    def prepareNonVegMeal():
        meal = Meal()
        meal.add(ChickenBurger())
        meal.add(Pepsi())
        return meal


if __name__ == '__main__':
    mealBuilder = MealBuilder()
    vegmeal = mealBuilder.prepareVegMeal()
    print(vegmeal.getCost())
    vegmeal.showItems()

    nonvegmeal = mealBuilder.prepareNonVegMeal()
    print(nonvegmeal.getCost())
    nonvegmeal.showItems()
