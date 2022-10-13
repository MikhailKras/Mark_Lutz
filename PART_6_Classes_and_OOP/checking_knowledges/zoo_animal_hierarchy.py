class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print('animal')


class Mammal(Animal):
    def speak(self):
        print('mammal')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('bark')


class Primate(Mammal):
    def speak(self):
        print('wow')


class Hacker(Primate):
    pass
