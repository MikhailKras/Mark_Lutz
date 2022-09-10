class Rec:
    pass


Rec.name = 'Bob'
Rec.age = 40
print(Rec.name)
x = Rec()
y = Rec()
print(x.name, y.name)
x.name = 'Sue'
print(Rec.name, x.name, y.name)
print(f'{list(Rec.__dict__.keys()) = }')
print(f'{[name for name in Rec.__dict__ if not name.startswith("__")] = }')
print(f'{list(x.__dict__.keys()) = }')
print(f'{list(y.__dict__.keys()) = }')
print(f'{x.__class__ = }')
print(f'{Rec.__bases__ = }')


def upper_name(obj):
    return obj.name.upper()


print(f'{upper_name(x) = }')
Rec.method = upper_name
print(f'{x.method() = }')
print(f'{Rec.method(x) = }')

