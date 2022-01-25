from turtle import width

import pygame as pg
from pygame.draw import rect, circle
from random import randrange  # строит случайный промежуток


W = 640  # размеры окна приложения
H = 480  # размеры окна приложения
WHITE = (255, 255, 255)  # цвета в RGB
BLUE = (0, 0, 255)  # цвета в RGB
ORANGE = (255, 175, 77)

obj_x = W // 2  # начальные координаты появления объекта
obj_y = H // 2  # начальные координаты появления объекта
change_x = 0  # смещение объекта по осям
change_y = 0  # смещение объекта по осям

c_x = randrange(40, W-40)  # помещаю круг в случайные координаты
c_y = randrange(40, H-40)  # помещаю круг в случайные координаты

s = pg.display.set_mode((W, H))  # экран приложения
clock = pg.time.Clock()

pg.display.update()
finished = False
while not finished:
    clock.tick(30)  # FPS
    for event in pg.event.get():  # обработчик событий
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:  # если нажали на кнопку
            print('Нажата кнопка', pg.key.name(event.key))  # вывожу название кнопки, которую нажали
            if event.key == pg.K_LEFT:  # если нажали на кнопку стрелка_влево
                change_x = -1  # уменьшаю х (иду влево)
                change_y = 0
            elif event.key == pg.K_RIGHT:  # если нажали на кнопку стрелка_вправо
                change_x = 1  # увеличиваю х (иду право)
                change_y = 0
            elif event.key == pg.K_UP:  # если нажали на кнопку стрелка_вверх
                change_y = -1  # уменьшаю у (иду вверх)
                change_x = 0
            elif event.key == pg.K_DOWN:  # если нажали на кнопку стрелка_вниз
                change_y = 1  # увеличиваю у (иду вниз)
                change_x = 0
            elif event.key == pg.K_ESCAPE:  # если нажали на кнопку стрелка
                change_x = 0

    obj_x += change_x
    obj_y += change_y

    if (obj_x > W) or (obj_x < 0) or (obj_y > H) or (obj_y < 0):  # если объект зашел за край экрана
        obj_x = W // 2 - 25
        obj_y = H // 2 - 25
        change_x, change_y = 0, 0

    if obj_x == c_x and obj_y == c_y:
        c_x = randrange(40, W - 40)
        c_y = randrange(40, W - 40)

    s.fill(WHITE)  # заливаем экран приложения белым цветом
    circle(s, BLUE, [obj_x, obj_y], 20)  # где_рисуем, (цвет в RGB), [x, y, width, height]
    circle(s, ORANGE, [c_x, c_y], 20)  # где_рисуем, (цвет в RGB), [x, y], radius
    pg.display.update()
