class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


x = Number(2)
y = Number(3)
z = Number(4)
acts = [x.double, y.double, z.double]
for act in acts:
    print(act())
bound = x.double
print(bound.__self__, bound.__func__)
