import pygame as pg
from pygame.draw import rect, aaline
import random as r


def moving(obj, speed, l_side, r_side):
    """
    Функция будет двигать машину по игровому полю.
    :param obj: игровой объект машина
    :param speed: скорость передвижения
    :param l_side: левая обочина
    :param r_side: правая обочина
    :return: None
    """
    obj.x += speed

    if obj.right >= r_side.left:  # если правый край машины коснулся левого края правой обочины
        obj.right = r_side.left - 5  # отодвинуть машину от правой обочины
    elif obj.left <= l_side.right:  # если левый край машины коснулся правой части левой обочины
        obj.left = l_side.right + 5  # отодвинуть машину от левой обочины


WHITE = (255, 255, 255)
GREEN = (13, 145, 59)
GRAY = (64, 64, 64)
SAND = (255, 244, 189)
RED = (209, 23, 39)

W = 800
H = 900

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Game objects
road = pg.Rect(0, 0, W // 2, H)
road.center = W // 2, H // 2
border_left = pg.Rect(road.x - W * 0.1, 0, W * 0.1, H)
border_right = pg.Rect(road.right, 0, W * 0.1, H)

road_width = road.width  # сохраняю ширину дороги
paddle = pg.Rect(road.x, -30, road_width * 0.3, 30)
paddle2 = pg.Rect(road.x, paddle.y - H // 2, road_width * 0.3, 30)

# Car
img = pg.image.load('car.png').convert_alpha()  # загружаю и импортирую в проект картинку машины
img_rect = img.get_rect()  # превращаю картинку в игровой объект
img_rect.center = 320, 800
car = img
car_rect = img_rect

# Tree
tree1 = pg.image.load('tree-3.png')
tree1_rect = tree1.get_rect()
tree1 = pg.transform.scale(tree1, [W * 0.1, H * 0.2])  # изменяю размер изображения
# scale(что_изменять, [ширина, высота])

tree2 = pg.image.load('tree-3.png')
tree2_rect = tree2.get_rect()
tree2 = pg.transform.scale(tree2, [W * 0.1, H * 0.2])

tree1_rect.x = 10
tree1_rect.y = 0 - H * 0.2
tree2_rect.x = W - 90
tree2_rect.y = 0 - H // 2

car_speed = 0  # начальная скорость машины
angle = 0  # угол поворота машины

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                car_speed += 10
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 10
                angle = 10
            car = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 10
                angle = 0
            if event.key == pg.K_LEFT:
                car_speed += 10
                angle = 0
            car = pg.transform.rotate(img, angle)

    # Visuals
    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [(W // 2) - (W * 0.01), 0, W * 0.02, H])  # линия разметки дороги
    rect(screen, RED, paddle)  # препятствие № 1
    rect(screen, RED, paddle2)  # препятствие № 2

    screen.blit(car, car_rect)  # отображаю картинку с машиной
    screen.blit(tree1, tree1_rect)
    screen.blit(tree2, tree2_rect)
    pg.display.update()

    # Game logic
    moving(car_rect, car_speed, border_left, border_right)
    paddle.y += 10
    paddle2.y += 10

    if paddle.top >= H:  # если препятствие упало вниз
        x = r.randint(1, 3)  # сгенерировать случайное число
        if x == 1:
            paddle.x = road.x  # первая дорожка
        elif x == 2:
            paddle.center = road.center  # вторая дорожка
        else:
            paddle.right = road.right  # третья дорожка
        paddle.y = -40  # поднять препятствие наверх
    if paddle2.top >= H:  # если препятствие упало вниз
        x = r.randint(1, 3)  # сгенерировать случайное число
        if x == 1:
            paddle2.x = road.x  # первая дорожка
        elif x == 2:
            paddle2.center = road.center  # вторая дорожка
        else:
            paddle2.right = road.right  # третья дорожка
        paddle2.y = paddle.y - H // 2  # поднять препятствие наверх

    tree1_rect.y += 10
    tree2_rect.y += 10
    if tree1_rect.y >= H:
        tree1_rect.y = 0 - H * 0.2
    if tree2_rect.y >= H:
        tree2_rect.y = 0 - H // 2

