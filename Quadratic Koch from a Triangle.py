import turtle

screen = turtle.Screen()
screen.title('Quadratic Koch Curve From Triangle by MuhammadShahsawar')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('midnight blue')
turtle.color('white')


def Koch(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if distance < 10:
        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)
        return

    turtle.up()
    turtle.goto(x1, y1)
    direction = turtle.towards(x2, y2)
    turtle.seth(direction)
    turtle.fd(distance/3)
    x3, y3 = turtle.xcor(), turtle.ycor()
    turtle.left(90)
    turtle.fd(distance/3)
    x4, y4 = turtle.xcor(), turtle.ycor()
    turtle.right(90)
    turtle.fd(distance/3)
    x5, y5 = turtle.xcor(), turtle.ycor()
    turtle.right(90)
    turtle.fd(distance/3)
    x6, y6 = turtle.xcor(), turtle.ycor()
    Koch(x1, y1, x3, y3)
    Koch(x3, y3, x4, y4)
    Koch(x4, y4, x5, y5)
    Koch(x5, y5, x6, y6)
    Koch(x6, y6, x2, y2)


Koch(500, -200, -500, -200)
Koch(-500, -200, 0, 500*3**0.5-200)
Koch(0, 500*3**0.5-200, 500, -200)
screen.update()
screen.exitonclick()
