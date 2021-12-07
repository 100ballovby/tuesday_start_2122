import requests as r

url = 'https://api.github.com/search/repositories'

try:
    parametrs = {'q': 'Django+language:python'}
    response = r.get(url, params=parametrs)
    json_r = response.json()
    for repo in json_r['items']:
        print(f'Name: {repo["name"]}, URL: {repo["html_url"]}')
except:
    print('Oh-oh! Error occurred while processing request')

