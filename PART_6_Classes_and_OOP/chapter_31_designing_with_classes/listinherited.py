class ListInherited:
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += f'\t{attr}\n'
            else:
                result += f'\t{attr}={getattr(self, attr)}\n'
        return result

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attrnames()}>'


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited, sept=True)

