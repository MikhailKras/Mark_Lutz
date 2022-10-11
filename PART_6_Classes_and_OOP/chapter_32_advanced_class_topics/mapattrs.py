"""
Главный инструмент: mapattrs() отображает все собственные и унаследованные атрибуты экземпляра на экземпляр или класс,
из которого они унаследованы.
Предполагает, что dir() выдает все атрибуты экземпляры.
Для эмуляции наследования использует либо кортеж MRO класса,
который дает порядок поиска для классов нового стиля
(и всех классов в Python 3.X), либо рекурсивный обход для выведения порядка DFLR классических классов в Python 2.X.
Также здесь: inheritance() дает нейтральный к версии порядок следования классов;
различные словарные инструменты, использующие включения Python 3.X/2.7.
"""
import pprint


def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)


def filterdictvals(D, V):
    return {K: V2 for (K, V2) in D.items() if V2 != V}


def inverdict(D):
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}


def dflr(cls: type):
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    if hasattr(instance.__class__, '__mro__'):
        return (instance, ) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def mapattrs(instance, withobject=False, bysource=False):
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else inverdict(attr2obj)


if __name__ == '__main__':
    print('Classic classes in 2.X, new-style in 3.X')

    class A: attr1= 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass
    I = D()
    print('Py=>%s' % I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
    print('New-style classes in 2.X abd 3.X')
    class A(object): attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass
    I = D()
    print('Py=>%s' % I.attr1)
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
