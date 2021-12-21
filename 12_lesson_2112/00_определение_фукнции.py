def say_hello():
    """Приветствует пользователя"""
    return 'Hello!'  # возврат результата работы
'''Определение функции ничего делать не будет.
Чтобы функция работала, нужно вызвать ее 
по имени. Пока функцию не вызвали, ее даже
не существует. Чтобы Python функцию создал,
функция должна быть вызвана в программном коде.'''
greet = say_hello()  # сохранить результат работы функции в переменную
print(greet)  # печатаю результат работы функции
print(greet[0])

# можно вывести информацию о функции
print(say_hello)  # обратите внимание на отсутствие скобок
print(say_hello)
print(say_hello)
'''Функция всегда хранится в одной ячейке памяти и сколько бы 
раз вы ее ни вызывали, она всегда будет там. Функции не создают 
клоны, когда вы вызываете их несколько раз, соответственно, она 
меньше задействует ресурсы, которые выдаются функции ОС.'''
