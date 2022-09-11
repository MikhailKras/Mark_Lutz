"""
Регистрирует и обрабатывает сведения о людях. Для тестирования классов из этого файла запустите его напрямую.
"""
from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Создает и обрабатывает записи о людях
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    Настроенная версия Person со специальными требованиями
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(f'{bob.name = } {bob.pay = }')
    print(f'{sue.name = } {sue.pay = }')
    print(f'{bob.last_name() = }', f'{sue.last_name() = }')
    print(sue)
    sue.give_raise(.10)
    print(f'{sue.pay}')
    print(f'{bob = }')
    print(f'{sue = }')
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(f'{tom.last_name() = }')
    print(f'{tom = }')
