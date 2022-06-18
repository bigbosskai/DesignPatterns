"""
组合模式（Composite Pattern），又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象。
组合模式依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，
它创建了对象组的树形结构。

这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。

我们通过下面的实例来演示组合模式的用法。实例演示了一个组织中员工的层次结构。
"""


class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.subordinates = []

    def add(self, e):
        self.subordinates.append(e)

    def remove(self, e):
        self.subordinates.remove(e)

    def getSubordinates(self):
        return self.subordinates

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.dept, self.salary)


if __name__ == "__main__":
    ceo = Employee("John", "CEO", 30000)
    head = Employee("Robert", "Headr Sal", 20000)
    headMarketing = Employee("Michel", "Head Marketing", 20000)

    clerk1 = Employee("Laura", "Marketing", 10000)
    clerk2 = Employee("Bob", "Marketing", 10000)

    salesExecutive1 = Employee("Richard", "Sales", 10000)
    salesExecutive2 = Employee("Rob", "Sales", 10000)

    ceo.add(head)
    ceo.add(headMarketing)

    head.add(salesExecutive1)
    head.add(salesExecutive2)

    headMarketing.add(clerk1)
    headMarketing.add(clerk2)

    for e in ceo.getSubordinates():
        print(e)
