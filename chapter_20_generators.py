# 1. В чем разница между помещением спискового включения в квадратные скобки
# и в круглые скобки?
answer1 = 'кв.: создается список, кр.: генератор'
# 2. Как связаны между собой генераторы и итераторы?
answer2 = 'подчиняются протоколу итерации (next())'
# 3. Как определить, является ли функция генераторной?
answer3 = 'yield'
# 4. Что делает оператор yield?
answer4 = 'заставляет питон компилить функцию как генераторную, функция поддерживает send, next'
# 5. Как связаны между собой вызовы mар и списковые включения? Сравните и противопоставьте их.
answer5 = 'map - применяют ф-ю к каждому элементу, создает генератор значений'


def myzip1(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def myzip2(*args):
    iters = list(map(iter, args))
    while iters:
        yield from [next(i) for i in iters]


s1 = [1,2,3,4,5]
s2 = 'asdfsadf'
res = myzip2(s1, s2)
print(res)
# print(myzip1(s1, s2))
