import json


def read_json(filename):
    with open(filename) as file:
        data = json.loads(file.read())
        data = data['data']['rates']
        return data


def get_rates(sequence, symbol):
    """
    Функция получает курс из словаря и возвращает его как значение
    :param sequence: последовательность (словарь)
    :param symbol: код валюты
    :return: курс
    """
    rate = 0
    message = ''
    try:
        rate = sequence[symbol.upper()]  # метод upper позволяет привести все буквы в верхний регистр
        message = 'Successfully!'
    except KeyError:
        rate = 0
        message = 'The currency you entered does not exist!'
    return rate, message


def exchange(amount, rate):
    """
    Считает количество денег для обмена
    :param amount: количество денег
    :param rate: курс валюты
    :return: сумма
    """
    res = amount * rate
    return res

db = read_json('rates.json')
answer = get_rates(db, 'BYN')
print(exchange(1500, answer[0]))
