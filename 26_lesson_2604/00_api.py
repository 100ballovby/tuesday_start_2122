import requests as r
import json

mode = 'latest'
key = ''  # сюда нужно поставить ключ 
base = 'USD'
symb = 'EUR,GBP,CNY,JPY,BYN,BTC'
url = f'https://commodities-api.com/api/{mode}?access_key={key}&base={base}'

response = r.get(url)
with open('rates.json', 'w') as file:
    file.write(response.text)  # записываю текст ответа сервера в файл

