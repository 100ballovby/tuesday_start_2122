import pygame as pg
from pygame.draw import circle, rect, polygon

WIN_WIDTH = 640
WIN_HEIGHT = 480
FPS = 30

colors = {
    'yellow': (255, 239, 61),
    'brick': (227, 180, 138),
    'dark_brick': (163, 132, 104),
    'sky_blue': (242, 255, 254),
    'grass_green': (60, 176, 83),
    'tree_green': (13, 120, 34),
    'dark_brown': (84, 59, 0),
    'blue': (132, 150, 207),
    'terracotta': (207, 156, 132),
    'dark_terr': (176, 132, 111),
}

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
finished = False

# рисую фон
rect(screen, colors['sky_blue'], [0, 0, WIN_WIDTH, WIN_HEIGHT * 0.6])
rect(screen, colors['grass_green'], [0, WIN_HEIGHT * 0.6, WIN_WIDTH, WIN_HEIGHT * 0.4])

# рисуем коробку дома
house_x = WIN_WIDTH * 0.1
house_y = WIN_HEIGHT * 0.4
house_length = WIN_WIDTH * 0.3
house_height = WIN_HEIGHT * 0.33

rect(screen, colors['brick'], [house_x, house_y, house_length, house_height])
rect(screen, colors['dark_brick'], [house_x - 5, house_y - 5,
                                    house_length + 5, house_height + 5], 5)

# рисую крышу
polygon(screen, colors['terracotta'], [
    [house_x - 20, house_y],
    [house_x + house_length + 20, house_y],
    [house_x + (house_length / 2), house_y - 80]
])
polygon(screen, colors['dark_terr'], [
    [house_x - 25, house_y],
    [house_x + house_length + 25, house_y],
    [house_x + (house_length / 2), house_y - 80]
], 5)

# рисуем дверь
door_x = house_x + house_length * 0.2
door_y = house_y + house_height * 0.4
rect(screen, colors['dark_brown'], [door_x, door_y,
                                    house_length * 0.25,
                                    house_height * 0.6])
circle(screen, colors['yellow'], [door_x + 35, door_y + 50], 5)

# рисуем окно
rect(screen, colors['blue'], [door_x + 65, door_y, 70, 60])
rect(screen, colors['dark_brick'], [door_x + 65, door_y, 70, 60], 5)

# солнце
circle(screen, colors['yellow'], [WIN_WIDTH * 0.8, WIN_HEIGHT * 0.2], WIN_HEIGHT * 0.15)

# елка
x = WIN_WIDTH * 0.7
y = WIN_HEIGHT * 0.55
base = WIN_WIDTH * 0.2
for triangle in range(3):
    polygon(screen, colors['tree_green'], [
        [x, y],
        [x + base, y],
        [x + (base / 2), y - 100]
    ])
    y += 50


pg.display.update()
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()

