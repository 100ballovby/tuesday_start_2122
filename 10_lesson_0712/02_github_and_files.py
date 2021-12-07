"""Необходимо найти все репозитории, где главным язком программирования
является Python. А затем вывести эти репозитории в формате:

Name: {name}
URL: {svn_url}
Language: {language}

!!!!🤩🤩🤩🤩!!!!
Сделать список словарей, который будет хранить всю
информацию из первой части задачи
"""
import json
import requests as r
from requests.exceptions import HTTPError

rep_log = []  # список репозиториев

try:
    url = 'https://api.github.com/users/GreatRaksin/repos'
    response = r.get(url)
    repos = json.loads(response.content)  # превращаю текс ответа в json-объект
    for repo in repos:  # перебираю все репозитории
        if repo['language'] == 'Python':  # если язык - Python
            print()
            print(f'Name: {repo["name"]}')
            print(f'URL: {repo["html_url"]}')
            print(f'Language: {repo["language"]}')

            rep_log.append({
                'name': repo["name"],
                'url': repo["html_url"],
                'language': repo["language"]
            })  # добавить ключевые части ответа в словарь, а словари добавлять в список

    json_object = json.dumps(rep_log, indent=4)  # список словарей превратить в JSON
    with open('greatraksin.json', 'w') as f:
        f.write(json_object)  # и записать его в файл

except HTTPError as e:
    print(f'Error occurred {e}')



