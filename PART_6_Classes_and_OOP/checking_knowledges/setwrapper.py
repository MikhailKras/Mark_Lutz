class Set:
    def __init__(self, value=None):
        if value is None:
            value = []
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)

    def __iter__(self):
        return iter(self.data)


class SubSet(Set):
    def intersect(self, *args):
        res = []
        for arg in args:
            for x in arg:
                if not x in res:
                    res.append(x)
        return Set(res)


if __name__ == '__main__':
    x, x1 = SubSet([1, 2]), Set([1, 2])
    y, y1 = SubSet([1, 3]), Set([1, 3])
    z, z1 = SubSet([1, 4]), Set([1, 4])
    print(x1 | y1 | z1 | x)
    print(x.intersect('123', [1, 2, 3], {5, 6}, (0, 0, 0)))
