class Singleton(object):

    def __new__(cls, *args, **kwargs):
        """
        在创建对象时会检查对象是否创建
        :param args:
        :param kwargs:
        """
        if not hasattr(cls, 'instance'):  # 检查对象是否包含instance属性
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(id(s))  # 4341452080
s2 = Singleton()
print(id(s2))  # 4341452080
