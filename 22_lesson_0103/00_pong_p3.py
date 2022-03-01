import pygame as pg
from pygame.draw import rect, ellipse, aaline
from random import choice


def ball_motion(obj, width, height, plr, enm):
    global ball_speed_x, ball_speed_y, p_score, o_score

    obj.x += ball_speed_x
    obj.y += ball_speed_y

    if obj.top <= 0 or obj.bottom > height:
        ball_speed_y *= -1
        pg.mixer.Sound.play(hit_sound)
    # Counting score
    elif obj.left <= 0:
        restart(obj, width, height)
        p_score += 1
        pg.mixer.Sound.play(score_sound)
    elif obj.right > width:
        restart(obj, width, height)
        o_score += 1
        pg.mixer.Sound.play(score_sound)

    elif obj.colliderect(plr) or obj.colliderect(enm):
        ball_speed_x *= -1
        pg.mixer.Sound.play(hit_sound)


def player_motion(plr, speed, height):
    plr.y += speed

    if plr.top <= 0:  # если платформа уперлась "в потолок"
        plr.top = 0  # зафиксировать ее верхнюю часть "на потолке"
    elif plr.bottom >= height:  # если платформа уперлась "в пол"
        plr.bottom = height  # зафиксировать ее нижнюю часть "на полу"


def opponent_ai(enm, speed, height, obj):
    """
    Функция автоматического передвижения платформы-оппонента
    :param enm: сама платформа
    :param speed: скорость передивжения
    :param height: высота экрана
    :param obj: игровой объект-мяч
    :return: None
    """
    if enm.top < obj.y:  # если платформа ниже мяча
        enm.y += speed  # поднять ее
    elif enm.bottom > obj.y:  # если платформа выше мяча
        enm.y -= speed  # опустить ее

    if enm.top <= 0:
        enm.top = 0
    elif enm.bottom >= height:
        enm.bottom = height


def restart(obj, width, height):
    """
    Функция перезагрузки игры в момент пропуска мяча одной из платформ
    :param obj: игровой-объект мяч
    :param width: ширина экрана
    :param height: высота экрана
    :return: None
    """
    global ball_speed_x, ball_speed_y

    obj.center = (width // 2, height // 2)
    ball_speed_x *= choice([-1, 1])  # скорость задается случайным числом из списка -1, 1
    ball_speed_y *= choice([-1, 1])  # скорость задается случайным числом из списка -1, 1

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

ball_speed_x = 7 * choice([-1, 1])
ball_speed_y = 7 * choice([-1, 1])
player_speed = 0
opponent_speed = 7

# Score text
pg.font.init()
p_score = 0
o_score = 0
basic_font = pg.font.SysFont('Comicsans', 32)

#Sound
pg.mixer.init()
hit_sound = pg.mixer.Sound('pong.ogg')
score_sound = pg.mixer.Sound('score.ogg')

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        if event.type == pg.KEYDOWN:  # если кнопку нажали
            if event.key == pg.K_UP:
                player_speed -= 7
            elif event.key == pg.K_DOWN:
                player_speed += 7
        if event.type == pg.KEYUP:  # если кнопку отпустили
            if event.key == pg.K_UP:
                player_speed += 7
            elif event.key == pg.K_DOWN:
                player_speed -= 7

    opponent_ai(opponent, opponent_speed, H, ball)
    player_motion(player, player_speed, H)
    ball_motion(ball, W, H, player, opponent)

    screen.fill(light_grey)
    rect(screen, cyan, player)  # игрок 1
    rect(screen, cyan, opponent)  # игрок 2
    ellipse(screen, cyan, ball)  # мячик
    aaline(screen, cyan, [W / 2, 0], [W / 2, H])  # разделительная линия

    p_text = basic_font.render(f'{p_score}', False, cyan)
    screen.blit(p_text, [W // 2 + 20, H // 2])

    o_text = basic_font.render(f'{o_score}', False, cyan)
    screen.blit(o_text, [W // 2 - 40, H // 2])

    pg.display.update()