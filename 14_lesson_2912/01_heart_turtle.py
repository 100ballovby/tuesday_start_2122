from turtle import *

t = Turtle()


def arc(turtle):
    for i in range(200):
        turtle.rt(1)
        turtle.fd(1)


def heart(turtle):
    turtle.fillcolor('red')  # выбрать цвет заливки фигуры
    turtle.begin_fill()  # начать заливку рисуемой фигуры

    turtle.lt(140)
    turtle.fd(113)

    arc(turtle)
    turtle.lt(120)
    arc(turtle)
    turtle.fd(113)

    turtle.end_fill()

heart(t)

t.up()
t.goto(-30, 100)
t.down()
t.color('white')
t.write('100ballov', font=('Calibri', 14, 'bold'))

done()