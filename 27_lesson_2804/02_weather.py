import requests as r
from datetime import datetime


api_key = '639cd74b40221a097d31bc5e64e343ab'
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {'q': 'Минск', 'appid': api_key,
          'units': 'metric', 'lang': 'ru'}

response = r.get(url, params=params)
print(response.text)
resp_json = response.json()
weather = f'''Погода в городе {resp_json["name"]}:
Температура: {resp_json["main"]["temp"]}, 
Ощущается как {resp_json["main"]["feels_like"]},
{resp_json["weather"][0]["description"]}'''
print(weather)
print(f'Рассвет: {datetime.fromtimestamp(resp_json["sys"]["sunrise"])}')
print(f'Закат: {datetime.fromtimestamp(resp_json["sys"]["sunset"])}')
