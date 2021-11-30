'''Режимы открытия файлов:
1) r - чтение (read)
2) w - запись (write)
3) w+ / r+ - чтение+запись (read-write)
4) a - добавление (append)
'''
with open('example.txt', 'w') as file:
    file.write('Привет! Я создал файлик!')

with open('example.txt', 'r') as file:
    print(file.read())

with open('example.txt', 'w') as file:
    file.write('Новый текст для файла!')

with open('example.txt', 'a') as file:
    text = '\nМеня добавили к старому тексту!\nПривет!'
    file.write(text)

