# 5
import random

print('Добро пожаловать в числовую угадайку!', 'Как вас зовут?')
name = str(input())
print(f'{name}, загадайте число от 1 до 10:')
num = random.randint(1, 11)
while True:
    n = int(input())
    while n not in range(1, num + 1):
        print('Вы ввели некорректное число! Введите еще раз!!')
        n = int(input())
    if n == num:
        print(f'Ура! Вы угадали - правильный ответ {num}.')
        break
    else:
        print('Пока неверно!')