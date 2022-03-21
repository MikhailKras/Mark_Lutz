# 1. Что выведет следующий код и почему?
# »> X = 'Spam'
# »> def func () :
# print(X)
# >» func ()
answer1 = 'Spam, ссылка на глобальную переменную'
# 2. Что выведет следующий код и почему?
# >» X = ' Spam’
# »> def func () :
# X = ’N1!’
# »> func ()
# >» print (X)
answer2 = 'Spam, в глобальной области'
# 3. Что выведет следующий код и почему?
# >» X = ’ Spam'
# »> def func () :
# X = ’N1’
# print(X)
# »> func ()
# »> print (X)
answer3 = 'N1, Spam'
# 4. Что выведет следующий код и почему?
# >» X - 'Spam'
# »> def func () :
# global X
# X = ’N1’
# »> func ()
# »> print (X)
answer4 = 'N1'
# 5. Что выведет следующий код и почему?
# »> X = ’ Spam’
# »> def func () :
#   X = ’N1’
#   def nested () :
#       print(X)
#   nested ()
# »> func()
# »> X
answer5 = 'N1, Spam'
# 6. Что выведет следующий код в Python З.Х и почему?
# >» def func () :
#   X = ’N1’
#   def nested () :
#       nonlocal X
#       X = ’Spam’
#   nested ()
#   print(X)
# »> func()
answer6 = 'Spam'
# 7. Назовите три или большее количество способов сохранения информации о состоянии в функции
# Python.
answer7 = 'атрибуты функций, классы, вложенные функции, стандартные значения аргументов'
