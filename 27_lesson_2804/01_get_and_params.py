import requests as r

url = 'https://google.com/search'
params = {'q': 'funny cats'}
response = r.get(url, params=params)

with open('cats.html', 'w') as file:
    file.write(response.text)
