from timer import bestoftotal
from timeit import timeit


def complexity_sqrt_n(y):
    if y > 1:
        if y % 2 == 0:
            return y, 'has factor', 2
        for i in range(3, round(y ** .5))[::1]:
            if y % i == 0:
                return y, 'has factor', i
        return y, 'is prime'
    return "is not prime and hasn't factor"


def complexity_n(y):
    if y > 1:
        x = y // 2
        while x > 1:
            if y % x == 0:
                return y, 'has factor', x
            x -= 1
        else:
            return y, 'is prime'
    else:
        return "is not prime and hasn't factor"


num = 97234346345734435771
# time_logn = bestoftotal(5, 10000, complexity_logn, num)
# time_n = bestoftotal(5, 10000, complexity_n, num)
# print(f'{time_n=}\n{time_logn=}\n{time_n > time_logn=}')
# print(complexity_n(num))
print(complexity_sqrt_n(num))

