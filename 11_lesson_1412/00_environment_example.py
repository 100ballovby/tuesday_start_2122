import os

for var in os.environ:
    print(f'Переменная: {var}\nЗначение: {os.environ.get(var)}\n')

t = os.environ.get('PWD')
print(t)
