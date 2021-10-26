n = int(input('Введите количество учеников: '))
marks = []

for mark in range(n):
    marks.append(int(
            input(f'Введите оценку {mark + 1} студента: ')
        ))

print(f'Среднее арифметическое: {sum(marks) / n}')


