# 3 заворачиваем в бесконечный цикл
name, age = str(input()), input()
while name:
    if age.isdigit() is True:
        if int(age) <= 0:
            print('Ошибка, повторите ввод')
        elif int(age) > 0 and int(age) < 10:
            print('Привет, шкет', name)
        elif 11 <= int(age) <= 18:
            print('Как жизнь', name, end='?')
        elif int(age) > 18 and int(age) < 100:
            print('Что желаете', name, end='?')
        else:
            print(name, ' вы лжете - в наше время столько не живут...', sep=',')
    else:
        print('Ошибка, повторите ввод')
