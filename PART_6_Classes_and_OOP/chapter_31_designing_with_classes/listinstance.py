class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\t{attr}={self.__dict__[attr]}\n'
        return result

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attrnames()}>'


if __name__ == '__main__':
    class Klass(ListInstance):
        def __init__(self, *args, **kwargs):
            for i, item in enumerate(args):
                exec(f'self.arg{i} = item')
            for i, kwitem in enumerate(kwargs):
                exec(f'self.kwarg{i} = kwitem')


    x = Klass(1, 2, 3, 4, a=1)
    print(x)
