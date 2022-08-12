import time
import random
from timer import total, bestof, bestoftotal


def timer(func, *args):
    start = time.time()
    for i in range(10000):
        func(*args)
    return time.time() - start


def gen_dct1(n1=0, n2=10):
    dct = {}
    for i in range(n1, n2):
        dct[i] = i ** 2
    return dct


def gen_dct2(n1=0, n2=10):
    return ((x, x ** 2) for x in range(n1, n2))


test1 = timer(gen_dct1)
test2 = timer(dict, gen_dct2()) + timer(gen_dct2)

print(test1, test2, sep='\n')

randlist1 = list(range(10000))
randlist2 = list(range(20000))
random.shuffle(randlist2)
randlist2 = randlist2[0:500]


def alg(list1: list, list2: list):
    """
    :return:
    """
    res = []
    for element2 in list2:
        for element1 in list1:
            if element2 == element1:
                res.append(element2)
    pass
    return len(res), res


# for i in range(10):
#     ret = alg(randlist1, randlist2)
#     print(alg(randlist1, randlist2), ret, sep='\n')
print(bestoftotal(10, 10, alg, randlist1, randlist2))
