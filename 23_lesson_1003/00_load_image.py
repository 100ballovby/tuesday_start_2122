import pygame as pg
from pygame.draw import rect, circle, polygon

W = 700
H = 1000

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

img = pg.image.load('bird.png').convert_alpha()  # загружает изображение в проект (в скобках имя файла)
# convert_alpha() включает прозрачность у фона изображения (если он прозрачный)
img_rect = img.get_rect()  # получаю квадрат картинки (делаю ее физическим объектом)

clone = img  # создаю клон изображения
clone_rect = img_rect  # создаю клон квадрата картинки
clone_rect.center = W // 2, H // 2  # располагаю изображение в центре экрана

angle = 0  # отвечает за поворот картинки
size = 1  # (1 = 100%), переменная отвечает за размер изображения

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    screen.blit(clone, clone_rect)  # отображаю картинку в ее квадрате
    pg.display.update()