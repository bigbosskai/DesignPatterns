class Student:
    """
    MVC中的m,model层
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


class StudentView:
    """
    MVC中的View
    """

    def printStuDetails(self, name, age):
        print(name, age)


class StudentController:
    """
    MVC中的Controller
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setName(self, name):
        self.model.setName(name)

    def updateView(self):
        self.view.printStuDetails(self.model.getName(), self.model.getAge())


if __name__ == '__main__':
    s = Student('tom', 12)
    controller = StudentController(s, StudentView())
    s.setName('Jerry')
    controller.updateView()
