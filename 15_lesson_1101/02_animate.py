import pygame as pg
from pygame.draw import circle


screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
finished = False

pg.display.update()
x_cor = 0
y_cor = 200
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    circle(screen, (191, 67, 81), [x_cor, y_cor], 50)  # рисую круг
    pg.display.update()

    if x_cor > 640:
        x_cor = 0
    else:
        x_cor += 5

