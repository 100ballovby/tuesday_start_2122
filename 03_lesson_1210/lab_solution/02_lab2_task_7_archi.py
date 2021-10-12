from turtle import *

t = Turtle()
t.shape('turtle')

fi_rad = 0.1  # угол "поворота" в радианах
k = 1  # "длина" дуги
fi_deg = fi_rad * (180 / 3.14)  # угол поворота !!!в градусах!!!

for i in range(1000):
    ring = k * fi_rad  # рассчитываю длину витка
    t.fd(ring)  # рисую виток
    t.lt(fi_deg)  # поворот на количество градусов, посчитанное в 8 строке

    fi_rad += 0.01
    ring += ring
done()