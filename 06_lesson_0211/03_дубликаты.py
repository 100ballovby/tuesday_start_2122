"""Написать программу, которая создает список,
элементы в котором не повторяются, но роодителем
для этого списка является другой список"""

foo = [1, 6, 11, 4, 1, 5, 5, 7, 11, 9, 4, 190, 56]
# [1, 6, 11, 4, 5, 7, 9, 190, 56]
bar = []
for number in foo:
    if number not in bar:
        bar.append(number)

print(bar)
