import json

with open('salaries.json') as f:
    data = json.loads(f.read())
    print(data)