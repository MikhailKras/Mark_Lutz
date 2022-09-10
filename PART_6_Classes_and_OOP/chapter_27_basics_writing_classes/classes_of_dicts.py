print(f'{20*"-"}Class-based record{20*"-"}', '', sep='\n')


class Rec:
    pass


Rec.name = 'Bob'
Rec.age = 40.5
Rec.jobs = ['dev', 'mgr']
print(f'{Rec.name = }')

print('', f'{20*"-"}Instance-based record{20*"-"}', '', sep='\n')


class Rec:
    pass


pers1 = Rec()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5
pers2 = Rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']
print(f'{pers1.name = }', f'{pers2.name = }', sep='\n')

print('', f'{20*"-"}Advanced-based record{20*"-"}', '', sep='\n')


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return self.name, self.jobs


rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])
print(f'{rec1.jobs = }', f'{rec2.info() = }', sep='\n')
