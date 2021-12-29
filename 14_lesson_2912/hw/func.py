def x_angle(turtle, x, y, corners, p_size=1, color='black', length=50):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.pensize(p_size)
    turtle.color(color)

    if corners >= 3:
        for line in range(corners):
            turtle.fd(length)
            turtle.lt(360 / corners)
    else:
        turtle.write('Меньше 3 углов не может быть!')
    return None


def spider(turtle, x, y, lines, length):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    for line in range(lines):
        turtle.fd(length)

        turtle.rt(30)
        x_angle(turtle, turtle.xcor(), turtle.ycor(), 3, 5)
        turtle.lt(30)

        turtle.bk(length)
        turtle.rt(360 / lines)


    return None