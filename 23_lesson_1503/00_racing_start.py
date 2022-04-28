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
road = pg.Rect(170, 0, 300, H)
border_left = pg.Rect(130, 0, 40, H)
border_right = pg.Rect(470, 0, 40, H)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    # Visuals
    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [316, 0, 8, H])  # линия разметки дороги

    # рисуем тут
    pg.display.update()