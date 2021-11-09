import random as r

r_list = []
for i in range(500):
    r_list.append(r.randint(-2000, 2000))

r_list.sort()
print(r_list)

key = int(input('Что ищем? '))

mid = len(r_list) // 2
low = 0
high = len(r_list) - 1

while r_list[mid] != key and low <= high:
    if key < r_list[mid]:
        high = mid - 1
    else:
        low = mid + 1
    mid = (low + high) // 2

if low > high:
    print('No value!')
else:
    print(f'ID = {mid}')
