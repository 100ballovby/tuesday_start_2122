import os

import requests


transl_url = "https://google-translate20.p.rapidapi.com/translate"
astro_url = 'https://sameer-kumar-aztro-v1.p.rapidapi.com/'

astro_headers = {
    'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('ASTRO_KEY')
}

transl_headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('GOOGLE_KEY')
}

lang = input('На каком языке вам нужен гороскоп? (es|fr|en|de|am|it|ru|zh)').lower()  # привожу в нижний регистр
sign = input('Введите свой знак зодиака: ').lower()  # привожу в нижний регистр
day = input('На какой день нужен гороскоп? (вчера|сегодня|завтра)').lower()

signs = {
    'овен': 'aries',
    'телец': 'taurus',
    'близнецы': 'gemini',
    'рак': 'cancer',
    'лев': 'leo',
    'дева': 'virgo',
    'весы': 'libra',
    'скорпион': 'scorpio',
    'стрелец': 'sagittarius',
    'козерог': 'capricorn',
    'водолей': 'aquarius',
    'рыбы': 'pisces',
}

sign = signs[sign]

if day == 'вчера':
    day = 'yesterday'
elif day == 'сегодня':
    day = 'today'
elif day == 'завтра':
    day = 'tomorrow'

astro_query = {'sign': sign, 'day': day}
astro_response = requests.post(astro_url,
                               headers=astro_headers,
                               params=astro_query)
a = astro_response.json()
a = a['description']

translate_query = f"text={a}&tl={lang}&sl=en"

translate_response = requests.post(transl_url,
                                   data=translate_query,
                                   headers=transl_headers)
print(translate_response.json())
