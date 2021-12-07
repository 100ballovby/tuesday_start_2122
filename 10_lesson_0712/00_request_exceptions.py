import json
import requests as r
from requests.exceptions import HTTPError


urls = ['https://google.com/erghfir',
        'https://api.github.com/kejgkr',
        'https://api.github.com/']

for url in urls:
    try:
        response = r.get(url)
        # когда запрос прошел, никаких ошибок не будет возникать
        response.raise_for_status()

        json_object = json.loads(response.content)  # метод "парсит" данные ответа. В качестве аргумента я передаю json-строку
        json_output = json.dumps(json_object, indent=4)  # загружаю спаршенный текст в json формат
        with open('github_api.json', 'w') as github:
            github.write(json_output)  # записываю получившийся json-объект в файл

        print(response.headers)

    except HTTPError as error:
        print(f'HTTP error occurred: {error}.')
    except Exception as other_error:
        print(f'Other error occurred: {other_error}')
    else:
        print(f'Successfully! Code: {response.status_code}')
