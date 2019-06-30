class stu:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def study(self, subject):
        print('I am studying class %s' % subject)

    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def info(self):
        print('my name is %s,I am %s year old' % (self.name, self.__age))
