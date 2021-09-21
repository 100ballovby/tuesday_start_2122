email = 'greatraksin@icloud.com'
email2 = 'GreatRaksin@iCloud.com'

# методы .lower() и .upper()
print(email2.lower())
print(email2.upper())

# методы .isupper(), .islower(), .isdigit()
print('f'.islower())  # True
print('A'.isupper())  # True
print('4.56'.isdigit())  # False

# метод .replace(a, b)
phrase = 'Привет! Я разработчик!'
print(phrase.replace('разработчик', 'пианист'))