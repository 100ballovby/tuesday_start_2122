from turtle import *

t = Turtle()
s = Screen()
t.shape('turtle')
s.bgcolor('black')

steps = 0.1
size = 1
for i in range(760):
    t.color('pink')
    t.pensize(size)
    t.lt(2)
    t.fd(steps)
    steps += 0.01
    size += 0.01

done()