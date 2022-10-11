class Set(list):
    def __init__(self, value=None):
        if value is None:
            value = []
        list.__init__(self)
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return f'Set:{list.__repr__(self)}'


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print(x, y, f'{len(x)=}')
    print(x.intersect(y), sorted(y.union(x)))
    print(x & y, x | y)
    x.reverse()
    y.sort()
    print(x)
    print(y)

