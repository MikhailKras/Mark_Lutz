from time import sleep
from chapter_21_estimated.timer import bestof, bestoftotal
from math import sqrt, factorial
from functools import reduce
from timeit import timeit
from sys import setrecursionlimit
# 1. Основы. Написать функцию, которая выводит единственный аргумент, и вызовите ее, передавая объекты разных типов:
# строку, целое число, список, словарь. Затем попробуйте вызвать ее без передачи какого-либо аргумента. Что произошло?
# Что происходит, когда передаются два аргумента?


def func(arg):
    return arg


ans1 = 'Возвращается аргумент, если не передать или передать больше одного, то TypeError'


# 2. Аргументы. Напишите функцию по имени adder в файле модуля Python. Функция должна принимать два аргумента
# и возвращать сумму (или результат конкантенации) их двух. Затем добавьте в конец файла код для вызова функции adder
# с объектами различных типов (две строки, два списка, два числа с плавающей точкой) и запустите файл как сценарий в
# окне командной строки системы. Требуется ли явно выводить результаты, чтобы видеть их на экране?


def adder1(x, y):
    return x + y


call1 = adder1('2', '3')
call2 = adder1(2, 3)
call3 = adder1([2, 3], [2, 3])
call4 = adder1(2.3, 3.2)
ans2 = 'Да, требуется'


# 3. Переменное количество аргументов. Обобщите написанную в предыдущем упражнении функцию adder,
# чтобы она вычисляла сумму произвольного количества аргументов, и измените вызовы для передачи более или менее двух аргументов.
# Какой тип имеет возвращаемое значение суммы? (Подсказки: срез вроде S[:0] возвращает пустую последовательность того же типа, что и S,
# а с помощью встроенной функции type можно проверять типы, но более простой подход ищите во вручную написанных примерах
# функции min в главе 18.) Что происходит при передаче аргументов отличающихся типов? Как насчет передачи словарей?


def adder2(*args):
    res = args[0]
    for i in args[1:]:
        res += i
    return res


call5 = adder2('2', '3', '4')
call6 = adder2(2, 3, 5)
call7 = adder2([2, 3], [2, 3], [1, 1, 1])
call8 = adder2(2.3, 3.2, 3.2, 2.3)
# print(call5, call6, call7, call8)
ans3 = 'Возвращаемая сумма имеет тот же тип, что и переданные аргументы. Словари не поддерживают операцию сложения, ' \
       'разные типы также нельзя сложить, поэтому будет TypeError'


# 4. Ключевые аргументы. Измените функцию adder из упражнения 2, чтобы она принимала и выполняла суммирование/конкатенацию трех аргументов:
# def adder(good, bad, ugly). Снабдите каждый аргумент стандартным значением и поэкспериментируйте с вызовом функции
# в интерактивной подсказке. Попробуйте передать один, два, три и четыре аргумента. Работает ли вызов adder (ugly=1, good=2)? Почему?
# Затем обобщите новую функцию adder с целью приема и выполнения суммирования/конкатенации для произвольного количества ключевых аргументов.
# Похожая работа делалась в упр. 3, но здесь нужно проходить по словарю, а не по кортежу.


def adder3(good=1, bad=2, ugly=3):
    return good + bad + ugly


ans4 = 'В функцию может быть передано от 0 до 3 аргументов, так как заданы стандартные значения для всех 3х аргументов'


def adder4(**kwargs):
    lst = list(kwargs.values())
    res = lst[0]
    for i in lst[1:]:
        res += i
    return res


# 5. Словарные инструменты. Написать функцию copyDict(dict), которая копирует свой аргумент типа словаря.
# Она должна возвращать новый словарь, содержащий все элементы из своего аргумента. Используйте для итерации словарный метод keys.
# Работает ли копирование словаря (dict[:])? Как объясняется в решении этого упражнения,
# поскольку словари теперь снабжены похожими инструментами, текущее и следующее упр. являются лишь тренировкой в написании кода,
# но служат характерными примерами функций.


def copydict(dct: dict) -> dict:
    solution1 = dct.copy()
    solution2 = {key: value for key, value in zip(dct.keys(), dct.values())}
    print(solution1 == solution2)
    return solution2


ans5 = 'Не работает, так как словари нехэшируемые объекты'


# 6. Словарные инструменты. см стр. 680


def add_dict(dict1, dict2):
    if isinstance(dict1, dict):
        return {**dict1, **dict2}
    elif isinstance(dict1, list):
        return [*dict1, *dict2]


# 7. Дополнительные примеры сопоставления аргументов. см стр. 680-681


def f1(a, b): print(a, b)  # Нормальные аргументы


def f2(a, *b): print(a, b)  # Переменное количество ключевых аргументов


def f3(a, **b): print(a, b)  # Переменное количество ключевых аргументов


def f4(a, *b, **c): print(a, b, c)  # Смешанные режимы


def f5(a, b=2, c=3): print(a, b, c)  # Стандартные значения


def f6(a, b=2, *c): print(a, b, c)  # Стандартные значения и переменное количество позиционных аргументов


# 8. Снова простые числа. см стр. 681


def is_prime(y):
    if y > 1:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x = x // 2
        else:
            print(y, 'is prime')
    else:
        print("is not prime and hasn't factor")


is_prime(111231)


# 9. Итерации и включения. см стр. 682
my_list = [2, 4, 9, 16, 25]


def for_loop(lst):
    res = []
    for i in lst:
        res.append(sqrt(i))
    return res


def map_call(lst):
    return list(map(sqrt, lst))


def list_comp(lst):
    return [sqrt(x) for x in lst]


def gen_exp(lst):
    return (sqrt(x) for x in lst)


# 10. Измерение времени выполнения инструментов. см стр. 682
num1 = 123562456982450624563457356784698679
reps1 = 10
reps2 = 10
time_sqrt = bestoftotal(reps1, reps2, sqrt, num1)
time_degrees = bestoftotal(reps1, reps2, lambda x: x**.5, num1)
time_pow = bestoftotal(reps1, reps2, pow, num1, .5)
min_time = min(time_sqrt, time_degrees, time_pow)[0]
print(f'{time_sqrt=}\n{time_degrees=}\n{time_pow=}', f'{min_time=}, sqrt', sep='\n')


# 11. Рекурсивные функции. стр 682


def countdown(number):
    # sleep(1)
    if number == 0:
        print('stop')
        return
    print(number)
    return countdown(number - 1)


# 12. Вычисление факториалов. стр 682
setrecursionlimit(5000)


def fact_recur(n):
    if n in (0, 1):
        return n
    return n * fact_recur(n-1)


def fact_reduce(n):
    return reduce(lambda x, y: x * y, range(2, n+1))


def fact_for(n):
    for i in range(2, n):
        n *= i
    return n


def fact_math(n):
    return factorial(n)


time_recur = timeit('fact_recur(1500)',
                    setup='def fact_recur(n):\n\tif n in (0, 1): return n\n\treturn n * fact_recur(n-1)',  number=1000)
time_reduce = timeit('fact_reduce(1500)',
                     setup='from functools import reduce\ndef fact_reduce(n):\n\treturn reduce(lambda x, y: x * y, range(2, n+1))',
                     number=1000)
time_for = timeit('fact_for(1500)', setup='def fact_for(n):\n\tfor i in range(2, n):\n\t\tn *= i\n\treturn n' , number=1000)
time_math = timeit('factorial(1500)', setup='from math import factorial' , number=1000)
print(f'{time_recur=}\n{time_reduce=}\n{time_for=}\n{time_math=}')