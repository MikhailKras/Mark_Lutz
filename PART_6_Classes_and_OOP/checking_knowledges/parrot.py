class Customer:
    def __init__(self):
        self.phrase = "that's one ex-bird!"
        print(f'{self.__class__.__name__}: "{self.phrase}"')


class Clerk:
    def __init__(self):
        self.phrase = "no it isn't..."
        print(f'{self.__class__.__name__}: "{self.phrase}"')


class Parrot:
    def __init__(self):
        self.phrase = None
        print(f'{self.__class__.__name__}: {self.phrase}')


class Scene:
    def action(self):
        self.cust = Customer()
        self.clerk = Clerk()
        self.parr = Parrot()


Scene().action()
