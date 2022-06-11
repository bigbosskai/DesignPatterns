class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print(Singleton.getInstance())  # <__main__.Singleton object at 0x101150ca0>

s1 = Singleton()
print(s1)  # <__main__.Singleton object at 0x101150c40>
