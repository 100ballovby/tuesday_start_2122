import pygame as pg
from pygame.draw import rect, ellipse, aaline

W = 1280
H = 960
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Pong game Python 🏓')
clock = pg.time.Clock()

light_grey = (176, 176, 176)
cyan = (93, 235, 240)

# game objects
ball = pg.Rect(W / 2 - 15, H / 2 - 15, 30, 30)
player = pg.Rect(W - 20, H / 2, 10, 140)
opponent = pg.Rect(20, H / 2, 10, 140)

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill(light_grey)
    rect(screen, cyan, player)  # игрок 1
    rect(screen, cyan, opponent)  # игрок 2
    ellipse(screen, cyan, ball)  # мячик
    aaline(screen, cyan, [W / 2, 0], [W / 2, H])  # разделительная линия

    pg.display.update()