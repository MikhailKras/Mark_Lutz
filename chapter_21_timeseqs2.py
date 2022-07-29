import sys, chapter_21_timer

reps = 10000
repslist = list(range(reps))


def for_loop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res


def list_comp():
    return [x + 10 for x in repslist]


def map_call():
    return list(map(lambda x: x + 10, repslist))


def gen_expr():
    return list(x + 10 for x in repslist)


def gen_func():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())


print(sys.version)
for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
    (bestof, (total, result)) = chapter_21_timer.bestoftotal(10, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
