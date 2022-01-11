import pygame as pg
from pygame.draw import rect, circle, polygon  # функции для рисования

screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
finished = False

screen.fill((255, 255, 255))  # заменить цвет фона

# нарисуем прямоугольник
rect(screen, (121, 93, 78), [50, 20, 110, 45])
rect(screen, (200, 151, 210), [10, 70, 50, 110], 6, 20)
# где_рисуем, (цвет в RGB), [x, y, ширина, высота], толщина_линии, скругление_углов

# нарисуем круг
circle(screen, (70, 110, 110), [110, 212], 50)
circle(screen, (219, 70, 219), [110, 212], 60, 5)
# где_рисуем, (цвет в RGB), [x, y], радиус, толщина_линии

# нарисуем треугольник
polygon(screen, (12, 78, 189), [[210, 180], [410, 180], [360, 100]])
polygon(screen, (12, 78, 189), [[210, 180], [410, 180], [360, 260]], 3)
# где_рисуем, (цвет в RGB), [[x1, y1], [x2, y2], [x3, y3]], толщина_линии

x = 100
y = 320
for i in range(10):
    circle(screen, (12, 78, 189), [x, y], 40, 7)
    x += 80

pg.display.update()
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()

