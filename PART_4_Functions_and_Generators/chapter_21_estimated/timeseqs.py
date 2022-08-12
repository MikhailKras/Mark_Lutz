import sys
import timer

reps = 10000
repslist = list(range(-2*reps, -reps))


def for_loop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def list_comp():
    return [abs(x) for x in repslist]


def map_call():
    return list(map(abs, repslist))


def gen_expr():
    return list(abs(x) for x in repslist)


def gen_func():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (bestof, (total, result)) = timer.bestoftotal(10, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
