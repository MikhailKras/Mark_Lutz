# 1. Какие выводы вы можете сделать из этой главы об относительной скорости итерационных инструментов Python?
ans1 = 'list comp - быстрее всех в общем случае; map выигрывает только тогда, когда все инструменты вызывают функции, ' \
       'for - медленнеее list comp, генераторы - тоже. В PyPy map часто показывает разную относительную производительность, ' \
       'list comp - самые быстрые, возможно, из-за оптимизаций на уровне функций'
# 2. Выводы об относительность скорости хронометрируемых версий Python?
ans2 = 'PyPy 1.9 быстрее CPython 2.7, а CPython 2.7 часто быстрее CPython 3.7'