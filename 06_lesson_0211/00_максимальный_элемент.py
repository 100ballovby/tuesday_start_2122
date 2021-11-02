nums = [1, 2, 3, 4, 5, 6]
maximum = 0
for num in nums:
    if num > maximum:
        maximum = num

print(maximum)
# ^ правильный

print(max(nums))  # однострочный
