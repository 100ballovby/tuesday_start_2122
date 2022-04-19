import json
import csv
import matplotlib.pyplot as plt

filename = 'series_NG.json'
dates = []
prices = []
with open(filename) as j_file:
    data = json.loads(j_file.read())
    data = data['data']['rates']
    for line in data:
        try:
            dates.append(line)
            prices.append(data[line]['NG'] * 28.263)
        except KeyError:  # если возникает ошибка несуществующего ключа
            pass  # ничего не делать

plt.title('Цены на газ за $1')
plt.xlabel('Дни')
plt.ylabel('Цены')
plt.grid()
plt.xticks(list(range(0, 126, 20)), rotation=45, fontsize=10)  # делаем подписи к осям реже
plt.plot(dates[69:], prices)  # обрезаю список с датами, чтобы сравнять длины списков

plt.savefig('gas.pdf')  # сохранить диаграмму в файл (расширение файла может быть любым)
plt.show()
