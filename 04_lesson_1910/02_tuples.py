my_tuple = (34, 12, 91, 75.5)
print(type(my_tuple))  # <class 'tuple'>

print(my_tuple[2])

wid, hei, lon, wei = my_tuple  # распаковка
print(wid, hei, lon, wei)

integers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a, b, *temp = integers
print(a, b, sep='!!!!')
print(temp, end='****я закончил****')

print(*integers, sep=' ⭐ ️')

for num in integers:
    print(num ** 2, end=', ')
