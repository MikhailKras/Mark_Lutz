# Числа
from decimal import *
from fractions import *

d = (hex(0b1111))
print(Decimal(1))
print(Fraction(16/5))
print(3602879701896397/1125899906842624)

# Строки
a = "Bob's"
b = b'a\x01c'
c = u'sp\xc4m'
print(a, b, c)

# Списки
f = list(range(5))
print(f)

# Кортежи
e = tuple('spam')
g = tuple('34545.34')
print(e, type(e), g, type(g))

# Множества
h = set('abc')
h1 = {'a', 'b', 'c'}
print(h == h1)

B = bytearray(b'spam')
B.extend(b'eggs')

print(type(str(B)), B)
print(B.decode())

