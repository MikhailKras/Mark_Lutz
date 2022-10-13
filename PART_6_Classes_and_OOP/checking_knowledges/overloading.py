from typing import Union
from sys import _getframe


class MyList:
    def __init__(self, data: Union[list, 'MyList'] = None):
        if data is None:
            data = []
        self.data = data

    def __add__(self, other: Union['MyList', list]) -> Union['MyList', list]:
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} {self.__class__.__name__} to {other.__class__.__name__}')
        return self.data + other

    def __radd__(self, other: Union['MyList', list]) -> Union['MyList', list]:
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} {self.__class__.__name__} to {other.__class__.__name__}')
        return other + self.data

    def __getitem__(self, item: Union[int, slice]):
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} for {self.__class__.__name__}')
        return self.data[item]

    def __iter__(self):
        self.ix = 0
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} for {self.__class__.__name__}')
        return self

    def __next__(self):
        if self.ix == len(self.data):
            raise StopIteration
        element = self.data[self.ix]
        self.ix += 1
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} for {self.__class__.__name__}, index = {self.ix}')
        return element

    def __str__(self):
        return str(self.data)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __len__(self):
        return len(self.data)

    def append(self, other):
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} for {self.__class__.__name__}')
        self.data.append(other)

    def sort(self, reverse=False):
        if self.__class__.__name__ == 'MyList':
            print(f'This used {_getframe().f_code.co_name} for {self.__class__.__name__}')
        if reverse:
            self.data.sort(reverse=True)
        else:
            self.data.sort()


x = MyList(MyList([1, 2]))
x + [1]
print(x[0:2])
print(5 in x)
x.append(10)
x.sort(False)
print(x)
y = x[:]
y.append(5)
print(y, type(y))
x.extend(['s'])
print(x)
