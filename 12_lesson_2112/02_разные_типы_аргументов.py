def power(n, deg=2):
    """Возводит n в степень deg"""
    res = 1
    for i in range(deg):
        res *= n
    return res


def divide(n, d):
    """Делит n на d"""
    try:
        n = int(n)
        d = int(d)
        res = n / d
        return res
    except ValueError:
        return 'Вы ввели не число!'
    except ArithmeticError:
        return 'На 0 нельзя делить!'

# позиционные аргументы
print(power(2, 9))
# поименные аргументы
print(power(deg=9, n=2))
# аргументы по умолчанию
print(power(5, 3))  # deg = 3
print(power(9, 7))  # deg = 7
print(power(10))  # deg = 2


print(divide(3234, 0))
print(divide(3234, 'erjgherjgh'))
print(divide(3234, 13))



