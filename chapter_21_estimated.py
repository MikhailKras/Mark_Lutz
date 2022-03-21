import time


def timer(func, *args):
    start = time.process_time()
    for i in range(10000):
        func(*args)
    return time.process_time() - start


def gen_dct1(n1=0, n2=10):
    dct = {}
    for i in range(n1, n2):
        dct[i] = i**2
    return dct


def gen_dct2(n1=0, n2=10):
    return ((x, x ** 2) for x in range(n1, n2))


test1 = timer(gen_dct1)
test2 = timer(dict, gen_dct2()) + timer(gen_dct2)

print(test1, test2, sep='\n')
