'''
try:
    do_smth()
except:
    do_another()

Type of exceptions:
ImportError - неправильно импортирована библиотека
IndexError - обращение к несуществующему индексу списка
NameError - неправильное имя переменной
TypeError - неправильно подобранный тип данных
ValueError - функция не получает аргумент правильного типа данных
ZeroDivisionError - деление 0
ArithmeticError - ошибка вычислений
'''
divider = int(input('Введите число: '))

try:  # попробовать выполнить это:
    print(31874 / divider)
except ArithmeticError:  # в случае возникновения исключения ошибки вычислений, делать это:
    print('На 0 делить нельзя!')

print('Привет! Спасибо!')
