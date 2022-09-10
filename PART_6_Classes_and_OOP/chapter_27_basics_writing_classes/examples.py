# first example
print(f'{20*"-"}First example{20*"-"}', '', sep='\n')


class FirstClass:
    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()
x.set_data('King Arthur')
y.set_data(3.14159)
x.display()
y.display()
x.data = 'New value'
x.display()
x.anothername = 'spam'


# second example
print('', f'{20*"-"}Second example{20*"-"}', '', sep='\n')


class SecondClass(FirstClass):
    def display(self):
        print(f'Current value = "{self.data}"')


z = SecondClass()
z.set_data(42)
z.display()


# third example
print('', f'{20*"-"}Third example{20*"-"}', '', sep='\n')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f'[ThirdClass: {self.data}]'

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)
a.mul(3)
print(a)
