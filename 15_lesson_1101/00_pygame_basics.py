import pygame as pg

# настроим игровое окно
screen = pg.display.set_mode((640, 480))  # размер окна 640x480 пикселей
clock = pg.time.Clock()  # отвечает за сменяемость кадров
finished = False  # пока finished = false, игра работает


# если нужно что-то отобразить на экране до запуска
pg.display.update()  # обновление экрана приложения
while not finished:  # пока игра не закрыта
    clock.tick(30)
    for event in pg.event.get():  # для каждого события в очереди событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    pg.display.update()  # обновление экрана внутри игрового цикла

