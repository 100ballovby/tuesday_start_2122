import pygame as pg
from pygame.draw import rect, circle, polygon

W = 400
H = 300
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

BLUE = (74, 143, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 74, 74)

x1 = 200  # змея появляется в этих координатах
y1 = 200  # змея появляется в этих координатах
x1_change = 0  # изменение положения змеи в пространстве
y1_change = 0  # изменение положения змеи в пространстве
snake_block = 10  # размер змеи
speed = 30

finished = False
while not finished:
    clock.tick(speed)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:  # если кто-то нажал на кнопку
            if event.key == pg.K_RIGHT:  # pg.K_d  wasd
                x1_change = snake_block
                y1_change = 0
            elif event.key == pg.K_LEFT:
                x1_change = -snake_block  # сдвигаю змею по горизонтали на расстояние, равное ее размеру
                y1_change = 0
            elif event.key == pg.K_UP:
                x1_change = 0
                y1_change = -snake_block  # сдвигаю змею по вертикали на расстояние, равное ее размеру
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = snake_block

    screen.fill(WHITE)
    rect(screen, BLUE, [x1, y1, snake_block, snake_block])
    pg.display.update()