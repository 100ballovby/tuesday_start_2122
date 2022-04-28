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

W = 640
H = 1000

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

# Game objects
road = pg.Rect(170, 0, 300, H)
border_left = pg.Rect(130, 0, 40, H)
border_right = pg.Rect(470, 0, 40, H)
paddle = pg.Rect(170, -30, 100, 30)

img = pg.image.load('car.png').convert_alpha()  # загружаю и импортирую в проект картинку машины
img_rect = img.get_rect()  # превращаю картинку в игровой объект
img_rect.center = 320, 800
car = img
car_rect = img_rect

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
                car_speed += 7
                angle = -10
            if event.key == pg.K_LEFT:
                car_speed -= 7
                angle = 10
            car = pg.transform.rotate(img, angle)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                car_speed -= 7
                angle = 0
            if event.key == pg.K_LEFT:
                car_speed += 7
                angle = 0
            car = pg.transform.rotate(img, angle)

    # Visuals
    screen.fill(GREEN)  # фон игры (трава)
    rect(screen, GRAY, road)  # дорога
    rect(screen, SAND, border_left)  # левая обочина
    rect(screen, SAND, border_right)  # правая обочина
    rect(screen, WHITE, [316, 0, 8, H])  # линия разметки дороги
    rect(screen, RED, paddle)  # препятствие

    screen.blit(car, car_rect)  # отображаю картинку с машиной
    rect(screen, (255, 0, 0), img_rect, 1)  # технические блоки, потом удалим
    rect(screen, (0, 255, 0), car_rect, 1)  # технические блоки, потом удалим
    pg.display.update()

    # Game logic
    moving(car_rect, car_speed, border_left, border_right)
    paddle.y += 8

    if paddle.top >= H:  # если препятствие упало вниз
        x = r.randint(1, 3)  # сгенерировать случайное число
        paddle.y = -40  # поднять препятствие наверх
        if x == 1:
            paddle.x = 170  # первая дорожка
        elif x == 2:
            paddle.x = 270  # вторая дорожка
        else:
            paddle.x = 370  # третья дорожка
