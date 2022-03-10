import pygame as pg
from pygame.draw import rect, circle, polygon

W = 700
H = 1000

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('bird.png').convert_alpha()
img_rect = img.get_rect()

clone = img
clone_rect = img_rect
clone_rect.center = W // 2, H // 2

angle = 0
size = 1

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_e]:
        angle += 10
        clone = pg.transform.rotate(img, angle)  # rotate(что_вращать, угол_вращения) - поворачивает изображение в пространстве
    if keys[pg.K_q]:
        angle -= 10
        clone = pg.transform.rotate(img, angle)

    screen.fill((255, 255, 255))
    screen.blit(clone, clone_rect)
    rect(screen, (255, 0, 0), img_rect, 1)
    pg.display.update()
