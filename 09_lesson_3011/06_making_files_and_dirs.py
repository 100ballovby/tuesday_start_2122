import os

try:
    os.mkdir('test_directory')  # Создаю новую папку
except FileExistsError:
    print('Папка создана!')

cwd = os.getcwd()  # получаю путь к текущей рабочей директории
work_path = os.path.join(cwd, 'test_directory')  # объединяю путь к директории с папкой
print(work_path)

for i in range(50):
    with open(os.path.join(work_path, f'file_{i}.py'), 'w') as f:
        f.write(f'print("Hello, world!")\nprint("file {i}")')


