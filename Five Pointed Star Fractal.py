import turtle
import math

screen = turtle.Screen()
screen.title('Five Pointed Star Fractal by MuhammadShahsawar')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(1)


def FivePointedStar(x, y, direction, r):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.fd(r)
    turtle.right(180-18)
    turtle.down()
    length = r*math.sin(math.pi*2/5)/(1+math.sin(math.pi/10))
    for _ in range(5):
        turtle.fd(length)
        turtle.left(72)
        turtle.fd(length)
        turtle.right(180-36)


def FivePointedStarFractal(x, y, direction, r):
    FivePointedStar(x, y, direction, r)
    if r < 20:
        return
    FivePointedStarFractal(x, y, 180+direction, r *
                           math.sin(math.pi/10)/math.cos(math.pi/5))


FivePointedStarFractal(0, -40, 90, 1000)
screen.exitonclick()