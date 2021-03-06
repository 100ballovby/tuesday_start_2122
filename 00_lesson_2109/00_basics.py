'''Функция input() позволяет взять значение
с клавиатуры и записать его в переменную.
Внутри скобочек можно написать вопрос, который
будет отображаться пользователю.

input() всегда возвращает вам строку.
'''

num1 = int( input('Введи число: ') )
num2 = int( input('Введи число: ') )

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)  # обычное деление 10 / 3 = 3.33333333
print(num1 // num2)  # целочисленное деление 10 // 3 = 3
print(num1 % num2)  # возврат остатка 10 % 3 = 1
print(num1 ** num2)  # возвести в степень
