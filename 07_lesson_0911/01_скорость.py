
import random as r
import time as t

search_me = [r.randint(-10000, 10000) for i in range(100000)]
search_me2 = [r.randint(-10000, 10000) for j in range(100000)]

search_me2.sort()


def linear(array, key):
    for i in range(len(array)):
        if array[i] == key:
            break
    return i



def binary(array, key):
    mid = len(array) // 2
    low = 0
    high = len(array) - 1

    while array[mid] != key and low <= high:
        if key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2

    if low > high:
        return 'No'
    else:
        return mid

start = t.time()
linear(search_me, 5000)
end = t.time()
print(f'Линейный: {end - start} сек.')

start1 = t.time()
binary(search_me2, 5000)
end1 = t.time()
print(f'Бинарный: {end1 - start1} сек.')
