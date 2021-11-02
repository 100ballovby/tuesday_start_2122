import random as r

r_list = []
for i in range(r.randint(5, 30)):
    r_list.append(r.randint(-100, 100))

print(r_list)
key = int(input('Что ищем? '))
res = None  # результата изначально нет

for i in range(len(r_list)):  # количество повторений цикла = длине списка
    if key == r_list[i]:
        res = i
        break   # принудительно выхожу из цикла

if res is not None:  # если не пустота
    print(f'Found! ID = {res}')
else:
    print('Not found!')
