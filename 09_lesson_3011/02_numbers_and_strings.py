'''Необходимо попросить пользователя наполнить список числами вручную.
Надо проверять, что это действительно число.'''
numbers = []
length = int(input('Введите длину списка: '))

while len(numbers) != length:
    try:
        n = int(input('Введи число: '))
        numbers.append(n)
    except ValueError:
        print('Это не число!')

print(numbers)

