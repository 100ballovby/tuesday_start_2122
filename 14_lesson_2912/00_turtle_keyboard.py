from turtle import *

t = Turtle()
screen = Screen()  # поле черепашки
screen.setup(600, 600)  # размер поля черепашки
screen.bgcolor('black')  # черный фон поля черепашки

t.shape('turtle')
t.color('white')

move_speed = 20
turn_speed = 20


def fd():
    t.fd(move_speed)
def bk():
    t.bk(move_speed)
def lt():
    t.lt(turn_speed)
def rt():
    t.rt(turn_speed)

t.speed()

screen.onkey(fd, 'Up')
screen.onkey(bk, 'Down')
screen.onkey(lt, 'Left')
screen.onkey(rt, 'Right')
screen.listen()

done()