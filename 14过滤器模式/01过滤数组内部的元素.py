from abc import ABCMeta, abstractmethod

"""
对过滤器做抽象
过滤器模式（Filter Pattern）或标准模式（Criteria Pattern）是一种设计模式，
这种模式允许开发人员使用不同的标准来过滤一组对象，通过逻辑运算以解耦的方式把它们连接起来。
这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。

下面的例子：
创建一个 Person 对象、Filter（翻译：标准） 接口和实现了该接口的实体类，
来过滤 Person 对象的列表。

"""


class Person:
    def __init__(self, name, gender, marital_status):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def isMarried(self):
        return self.marital_status

    def __str__(self):
        return "name:{}\tgender:{}\tisMarried:{}".format(self.name, self.gender, self.marital_status)


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, persons_lst):
        pass


class MaleFilter(Filter):
    def filter(self, persons_lst):
        new_persons = []
        for p in persons_lst:
            if p.getGender() == '男':
                new_persons.append(p)
        return new_persons


class FemaleFilter(Filter):
    def filter(self, persons_lst):
        new_persons = []
        for p in persons_lst:
            if p.getGender() == '女':
                new_persons.append(p)
        return new_persons


class SingleFilter(Filter):
    def filter(self, persons_lst):
        new_persons = []
        for p in persons_lst:
            if not p.isMarried():
                new_persons.append(p)
        return new_persons


class OrFilter(Filter):
    def __init__(self, criteria, other_criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def filter(self, persons_lst):
        persons = self.criteria.filter(persons_lst)
        other_persons = self.other_criteria.filter(persons_lst)
        for p in other_persons:
            if p not in persons:
                persons.append(p)
        return persons


class AndFilter(Filter):
    def __init__(self, criteria, other_criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def filter(self, persons_lst):
        persons = self.criteria.filter(persons_lst)
        other_persons = self.other_criteria.filter(persons)
        return other_persons


def print_persons(persons):
    for p in persons:
        print(p)


if __name__ == '__main__':
    person_lst = []
    person_lst.append(Person("Robert", "男", True))
    person_lst.append(Person("John", "女", False))
    person_lst.append(Person("Laura", "女", True))
    person_lst.append(Person("Diana", "女", False))
    person_lst.append(Person("Mike", "男", True))
    person_lst.append(Person("Bobby", "男", False))

    male = MaleFilter()
    print_persons(male.filter(person_lst))

    female = FemaleFilter()
    print_persons(female.filter(person_lst))

    single_male = AndFilter(MaleFilter(), SingleFilter())
    print_persons(single_male.filter(person_lst))
