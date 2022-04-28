import requests as r

url = 'https://google.com/'
response = r.get(url)
# print(response.headers)  <- дополнительная информация об ответе
# print(response.content)  <- содержимое ответа в битовом виде
with open('google_responce.html', 'w') as file:
    file.write(response.text)

