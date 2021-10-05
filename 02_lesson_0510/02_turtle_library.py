from turtle import *

t = Turtle()  # создал объект черепашки
t.shape('turtle')  # черепашка выглядит как черепашка

for i in range(4):
    t.fd(100)  # идти вперед на 100 точек
    t.rt(90)  # повернуть вправо на 90 градусов

t.up()  # поднять перо (не рисовать)
t.goto(200, -200)  # перейти в координаты 200;-200
t.down()  # опустить перо

# TODO: нарисовать прямоугольник
for i in range(2):
    t.fd(100)  # идти вперед на 100 точек
    t.rt(90)  # повернуть вправо на 90 градусов
    t.fd(50)
    t.rt(90)

t.up()  # поднять перо (не рисовать)
t.goto(-100, 200)  # перейти в координаты 200;-200
t.down()  # опустить перо

# TODO: нарисовать треугольник
for i in range(3):
    t.fd(100)
    t.lt(120)

t.circle(80)  # нарисовать окружность с диаметром 80
t.dot(50)  # нарисовать круг с диаметром 50

done()  # чтобы окно не закрывалось сразу

