import random as r

secret_number = r.randint(1, 100)
name = input(f'Привет! Как тебя зовут?')
print(f'Привет, {name.capitalize()}! Я загадал число от 1 до 100. Угадай его.')
# метод .capitalize() пишет строчку с большой буквы. остальные маленькие
guessTaken = 0
guess = None

while guessTaken <= 7 and guess != secret_number:
    guessTaken += 1
    guess = int(input('Введи число: '))
    if guess > secret_number:
        print('Слишком много!')
    elif guess < secret_number:
        print('Слишком мало!')

if guess == secret_number:
    print('Молодец!')
else:
    print(f'Ты не угадал! Это было число: {secret_number}!')