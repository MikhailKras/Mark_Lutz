class Indexer:
    def __getitem__(self, item):
        return item ** 2


class Indexer2:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        print('getitem', item)
        return self.data[item]


x = Indexer2()
print(x[2:4])


class Indexer3:
    def __getitem__(self, item):
        if isinstance(item, int):
            print('indexing', item)
        elif isinstance(item, slice):
            print('slicing', item.start, item.stop, item.step)


x = Indexer3()
print(x[2:4], x[99])


class SteperIndex:
    def __getitem__(self, item):
        return self.data[item]


x = SteperIndex()
x.data = 'Spam'
print(x[1])
for item in x:
    print(item, end=' ')


