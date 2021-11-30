import os

# я получу путь к папке, в которой работает мой файл
cwd = os.getcwd()  # сохраняю путь к текущей папке
print(f'Current working directory is {cwd}')

# чтобы просмотреть содержимое:
entries = os.listdir(cwd)  # просматриваю все вложенные элементы cwd
print(entries)

for file in entries:  # просматриваю каждый объект в проекте
    try:
        with open(file, 'r') as f:  # Открываю файл в режиме чтения
            print(f.read(), '\n\n\n')  # и читаю его
    except PermissionError:
        pass


