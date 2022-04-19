import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [150, 95, 73, 101, 112]
y1 = [210, 120, 56, 43, 28]

plt.title('Линейная зависимость')  # название диаграммы
plt.xlabel('Дни')  # подпись к оси
plt.ylabel('Количество')  # подпись к оси
plt.grid()  # включить сетку
plt.plot(x, y, y1, color='#34ebc6',
         linewidth=5,  # толщина линии графика
         linestyle='dotted',  # стиль линии графика
         marker='*',  # вид ключевой точки на графике
         markersize=20)  # линейная диаграмма
plt.show()  # показать диаграмму

