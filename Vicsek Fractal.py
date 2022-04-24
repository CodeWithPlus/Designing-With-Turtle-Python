import turtle

screen = turtle.Screen()
screen.title('Vicsek Fractal by MuhammadShahsawar')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)
turtle.speed(0)
turtle.hideturtle()
turtle.color('blue')


def DrawCross(x, y, length):
    turtle.up()
    turtle.goto(x-length/2, y-length/6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length/3)
        turtle.right(90)
        turtle.fd(length/3)
        turtle.left(90)
        turtle.fd(length/3)
        turtle.left(90)
    turtle.end_fill()


def Vicsek(x, y, length, n):
    if n == 0:
        DrawCross(x, y, length)
        return

    Vicsek(x, y, length/3, n-1)
    Vicsek(x+length/3, y, length/3, n-1)
    Vicsek(x-length/3, y, length/3, n-1)
    Vicsek(x, y+length/3, length/3, n-1)
    Vicsek(x, y-length/3, length/3, n-1)


Vicsek(0, 0, 1600, 5)
screen.update()
screen.exitonclick()
