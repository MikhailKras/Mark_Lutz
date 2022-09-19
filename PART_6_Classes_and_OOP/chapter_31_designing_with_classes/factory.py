def factory(aClass: type, *args, **kwargs):
    return aClass(*args, **kwargs)


if __name__ == '__main__':
    class Klass:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        def method(self):
            print(f'{self.args = }, {self.kwargs = }, {Klass.__name__ = }')

    x = factory(Klass, 1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)
    x.method()
