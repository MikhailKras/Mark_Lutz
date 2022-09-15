from typing import Sequence


class Iters:
    def __init__(self, value: Sequence):
        self.data = value

    def __getitem__(self, item):
        print(f'get [{item}]:', end=' ')
        return self.data[item]

    def __iter__(self):
        print('iter=>', end=' ')
        for x in self.data:
            yield x
            print('next:', end=' ')

    def __contains__(self, item):
        print('contains:', end=' ')
        return item in self.data


if __name__ == '__main__':
    var = Iters([1, 2, 3, 4, 5])
    print('3' in var)
    for i in var:
        print(i, end=' | ')
    print()
    print([i ** 2 for i in var])
    print(list(map(bin, var)))
    items = iter(var)
    while True:
        try:
            print(next(items), end=' @ ')
        except StopIteration:
            break
    print(dir(var))
