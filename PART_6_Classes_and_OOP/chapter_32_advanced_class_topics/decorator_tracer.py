import types


class tracer:
    def __init__(self, func: types.FunctionType):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
