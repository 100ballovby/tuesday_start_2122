from turtle import *
import math

t = Turtle()
t.shape('turtle')

fi_rad = 0.1  # угол "поворота" в радианах
k = 1  # "длина" дуги

for i in range(1000):
    ring = k * fi_rad  # рассчитываю длину витка
    x = math.cos(fi_rad) * ring
    y = math.sin(fi_rad) * ring

    t.goto(x, y)

    fi_rad += 0.1
done()