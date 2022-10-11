def count_inst(cls):
    cls.calls = 0

    def wrapper(*args, **kwargs):
        cls.calls += 1
        print(f'{cls.calls=}')
        return cls(*args, **kwargs)

    return wrapper


@count_inst
class A:
    def __init__(self, name):
        self.name = name


x = A('Bob')
y = A('Jack')
