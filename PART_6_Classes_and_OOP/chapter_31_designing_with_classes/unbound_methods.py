class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(*args):
        print(f'This is {Selfless.selfless.__name__}')
        return sum(args)

    def normal(self, *args):
        print(f'This is {self.normal.__name__}')
        return self.data + sum(args)


x = Selfless(2)
print(x.normal(1, 3, 5, 7))
print(Selfless.normal(x, 1, 3, 5, 7))
print(Selfless.selfless(3, 5, 9))
# print(x.selfless(2)) # TypeError: unsupported operand type(s) for +: 'int' and 'Selfless' (x - является аргументом функции)
# print(Selfless.normal(3, 4)) # AttributeError: 'int' object has no attribute 'normal' (метод ожидает экземпляр на месте первого аргумента)
