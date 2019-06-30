class Sutdent(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def create(cls):
        return cls("haha", 18)

    def info(self):
        print("haha")
        # print("my name is %s, I am %d year old" % (self._name, self._age))
