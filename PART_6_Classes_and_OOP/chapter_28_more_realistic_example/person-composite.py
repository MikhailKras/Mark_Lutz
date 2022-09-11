class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f'[Person: {self.name}, {self.pay}]'


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(f'{bob.name = } {bob.pay = }')
    print(f'{sue.name = } {sue.pay = }')
    print(f'{bob.last_name() = }', f'{sue.last_name() = }')
    print(sue)
    sue.give_raise(.10)
    print(f'{sue.pay}')
    print(bob)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(f'{tom.last_name() = }')
    print(f'{tom = }')

