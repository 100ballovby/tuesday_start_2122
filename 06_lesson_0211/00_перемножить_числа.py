"""Перемножить все элементы списка"""
nums = [1, 2, 3, 4, 5, 6]
mult = 1  # перемножение тут
for element in nums:
    mult *= element

print(f'Произведение: {mult}')
