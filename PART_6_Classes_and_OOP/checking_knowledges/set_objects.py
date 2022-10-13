from setwrapper import Set

x = Set([1, 1, 2, 3, 4, 4, 5, 6, 6])  # __init__
y = Set([10, 1, 11, 3, 15])
print(x & y)  # __and__
print(x | y)  # __or__
z = Set('hello')  # __init__
print(z[0], z[-1], z[2:])  # __getitem__
for i in z:
    print(i, end=' ')
print(len(z))
print(Set('123') & '345')

