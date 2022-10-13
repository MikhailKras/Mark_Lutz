# Inheritance
class Adder:
    def add(self, x, y):
        print('Not Implemented')

    def __init__(self, start=None):
        if start is None:
            start = []
        self.data = start

    def __add__(self, other):
        print('This used __add__ from Adder')
        return self.add(self.data, other)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y  # x.__add__(y)


class DictAdder(Adder):
    def add(self, x, y):
        return {**x, **y}


if __name__ == '__main__':
    x = ListAdder()
    print(x.add([1, 2], [0, 7]))
    y = ListAdder(['s', (1, 2)])
    print(y + [1, 2])

