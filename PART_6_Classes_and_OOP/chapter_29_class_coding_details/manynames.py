x = 11


def f():
    print(x)


def g():
    x = 22
    print(x)


class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55


if __name__ == '__main__':
    print(f'{x = }')
    f()
    g()
    print(f'{x = }')
    obj = C()
    print(f'{obj.x = }')
    obj.m()
    print(f'{obj.x = }')
    print(f'{C.x = }')