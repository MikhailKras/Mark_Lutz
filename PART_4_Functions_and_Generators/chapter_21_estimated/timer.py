import time

timer = time.time


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times
    :return: (total time, last result)
    """
    repsrange = range(reps)
    start = timer()
    for i in repsrange:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps times
    :return: (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return round(best, 3), ret


def bestoftotal(reps1, reps2, func, *args, **kwargs):
    """
    Best of reps1 runs of (total of reps2 runs of func)
    """
    return bestof(reps1, total, reps2, func, *args, **kwargs)
