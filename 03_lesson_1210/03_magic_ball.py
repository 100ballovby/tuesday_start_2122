"""Нужно написать программу, которая поможет
пользователю принять решение. Человек задает вопрос,
а программа выдает ответ: да, нет или наверное"""
import random as r

question = input('Задай свой вопрос: ')
answer = r.randint(1, 3)  # 3 числа, потому что 3 варианта ответа

if answer == 1:  # если сгенерировалось число 1
    print('Да!')
elif answer == 2:  # иначе если сгенерировалось число 2
    print('Нет!')
else:  # иначе (если сгенерировалось число 3)
    print('Наверное...')


