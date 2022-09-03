#!python
"""
mydir.py: модуль, который выводит листинг пространства имен другого модуля
"""
seplen = 60
sepchr= '-'


def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)
    count = 0
    for attr in sorted(module.__dict__):  # Просмотр ключей пространств имен (или перечисление)
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')  # Пропуск dunders
        else:
            print(getattr(module, attr))
        count += 1
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    import mydir
    listing(mydir)  # Код самотестирования: список для самого себя