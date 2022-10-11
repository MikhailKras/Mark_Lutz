class Methods:

    def imeth(self, x):
        print([self, x])

    @staticmethod
    def smeth(x):
        print([x])

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return 'Bob' + self.__class__.__name__


obj = Methods()
obj.imeth(1)
obj.smeth(2)
name = obj.name
print(name)
