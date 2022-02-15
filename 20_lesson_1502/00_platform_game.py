import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (237, 107, 28)

speed = 15

player_x = W // 2
player_y = H - 100

radius = 40
circle_x = randint(0, W)
circle_y = 0 - radius

pg.font.init()
font = pg.font.SysFont('comicsans', 32)
score = 3

finished = False
game_over = False
while not finished:  # пока игра не окончена

    while game_over:
        screen.fill(WHITE)
        txt = font.render('Press C to continue or ESC to exit', True, BLACK)
        screen.blit(txt, [W // 2, H // 2])
        pg.display.update()
        for event in pg.event.get():  # для каждого события в списке событий
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    game_over = False
                    score = 3
                if event.key == pg.K_ESCAPE:
                    pg.quit()

    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    screen.fill(WHITE)
    platform = rect(screen, BLACK, [player_x, player_y, 200, 50])
    enemy = circle(screen, RED, [circle_x, circle_y], radius)

    txt = font.render(f'Score: {score}', True, BLACK)
    screen.blit(txt, [0, 0])
    # рисуем тут
    pg.display.update()

    # движение платформы
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player_x += speed + 4
    if keys[pg.K_LEFT]:
        player_x -= speed + 4

    #  движение шарика
    circle_y += speed
    if circle_y > H:
        circle_y = 0 - radius
        circle_x = randint(0, W)
        score -= 1

    # коллизия платформы
    if platform.colliderect(enemy):
        circle_y = 0 - radius
        circle_x = randint(0, W)
        score += 1

    # условие проигрыша
    if score <= 0:
        game_over = True
    print(speed)
    # увеличение скорости
    if score > 0 and score % 10 == 0:
        score += 1
        speed += 1
