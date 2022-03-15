import pygame as pg
from pygame.draw import rect, aaline

WHITE = (255, 255, 255)
GREEN = (13, 145, 59)
GRAY = (64, 64, 64)
SAND = (255, 244, 189)
RED = (209, 23, 39)

W = 640
H = 1000

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Game objects


finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # рисуем тут
    pg.display.update()