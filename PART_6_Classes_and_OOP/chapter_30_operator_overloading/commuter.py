import inspect


class Represent:
    def __repr__(self):
        return f'{40*"-"}\nval = {self.val} This is {self.__class__.__name__}'


class Commuter1(Represent):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self)
        return self.val + other

    def __radd__(self, other):
        print(inspect.currentframe().f_code.co_name.replace('_', ''), self)
        return other + self.val


class Commuter2(Represent):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)


class Commuter3(Represent):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other


class Commuter4(Represent):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    __radd__ = __add__


class Commuter5(Represent):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)

    def __radd__(self, other):
        return Commuter5(other + self.val)


if __name__ == '__main__':
    classes = (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5)
    for klass in classes:
        x = klass(2)
        y = klass(3)
        x += 1
        print(x)

