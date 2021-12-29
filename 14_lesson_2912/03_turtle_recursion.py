from turtle import *


def draw_circle(turtle, size, angle, shift):
    if size == 100:
        return 0
    else:
        turtle.circle(size)
        turtle.rt(angle)
        turtle.fd(shift)

        draw_circle(turtle, size + 5, angle + 1, shift + 1)


t = Turtle()
t.speed(0)
draw_circle(t, 5, 0, 1)


done()
