from overloading import MyList


class MyListSub(MyList):
    calls = 0

    def __init__(self, data=None):
        super().__init__(data)
        self.counter = 0

    def __add__(self, other):
        MyListSub.calls += 1
        self.counter += 1
        print(f'{self.counter=}, {self.calls=}')
        return self.data + other

    def get_counter(self):
        return self.counter, self.calls


x = MyListSub([99, 100])
for i in range(10):
    x + [i]
    x.append(i)
print(x[1:], x[2])
print(x.get_counter())
y = MyListSub()
print(y.get_counter())