# way number 1
class Retainer:
    def __init__(self, name='Michael'):
        self.name = name

    def __call__(self):
        return f'retain state = {self.name}'


# way number 2
retain_lambda = (lambda name='Michael': f'retain state = {name}')


# way number 3
def retain_def(name='Michael'):
    def inner_func():
        return f'retain state = {name}'
    return inner_func


if __name__ == '__main__':
    ways = [Retainer(), retain_lambda, retain_def()]
    print(([way() for way in ways]))
