import typing


class Food:
    def __init__(self, name: str):
        self.name = name
        print(f'{self.name} is cooked')


class Employee:
    @staticmethod
    def take_order(food_name: str) -> 'Food':
        print(f'employee took order on {food_name}')
        return Food(food_name)


class Customer:
    def __init__(self):
        self.my_food = None

    def place_order(self, food_name: str, employee: 'Employee'):
        print(f'customer ordered {food_name}')
        self.my_food = employee.take_order(food_name)

    def print_food(self):
        print(self.my_food)


def count_order(func: typing.Callable) -> typing.Callable:
    num_order = 0

    def wrapper(*args, **kwargs):
        nonlocal num_order
        num_order += 1
        print('-'*20)
        print(f'init {func.__name__} #{num_order}')
        return func(*args, **kwargs)

    return wrapper


class Lunch:
    def __init__(self):
        self.num_order = 0
        self.customer = Customer()
        self.employee = Employee()
        print(f'new customer {str(id(self.customer))[-4:]} and employee {str(id(self.employee))[-4:]} was created!')

    @count_order
    def order(self, food_name):
        self.customer.place_order(food_name, self.employee)

    def result(self):
        self.customer.print_food()


x = Lunch()
x.order('chicken with potatoes')
x.order('tomatoes')
x.order('apples')
y = Lunch()
y.order('eggs')
z = Lunch()
z.order('cakes')
z.result()
y.result()
