# 3 заворачиваем в бесконечный цикл
name, age = str(input()), int(input())
while age:
    if age <= 0 or age is str:
        print('Ошибка, повторите ввод')
    elif age > 0 and age < 10:
        print('Привет, шкет', name)
    elif 11 <= age <= 18:
        print('Как жизнь', name, end='?')
    elif age > 18 and age < 100:
        print('Что желаете', name, end='?')
    else:
        print(name, ' вы лжете - в наше время столько не живут...', sep=',')