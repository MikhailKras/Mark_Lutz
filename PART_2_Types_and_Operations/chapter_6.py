# 1. Взгляните на следующие три оператора. Изменяют ли они значение, выводимое для А?
# А = "spam”
# В = А
# В = "shrubbery"
answer1 = False
# 2. Взгляните на приведенные ниже три оператора. Изменяют ли они значение, выводимое для А?
А = ["spam"]
В = А
В[0] = "shrubbery"
answer2 = True
# 3. Как насчет показанных далее трех операторов — изменяется ли А теперь?
# А= ["spam"]
# В = А[:]
# В[0] = "shrubbery"
answer3 = False