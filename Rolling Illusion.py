import turtle
import math

screen = turtle.Screen()
screen.setup(1100, 1000)
screen.setworldcoordinates(-620, -550, 680, 550)
screen.tracer(0, 0)
screen.title('Roller Illusion by MuhammadShahsawar')
turtle.hideturtle()
turtle.speed(0)
n = 100


def Ellipse(cx, cy, a, b, c1, c2, c3):
    t = -math.pi/2
    x = cx+a*math.cos(t)
    y = cy+b*math.sin(t)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(c1)
    turtle.fillcolor(c3)
    turtle.begin_fill()
    for i in range(n//2):
        x = cx+a*math.cos(t)
        y = cy+b*math.sin(t)
        turtle.goto(x, y)
        t += 2*math.pi/n
    turtle.pencolor(c2)
    for i in range(n//2):
        x = cx+a*math.cos(t)
        y = cy+b*math.sin(t)
        turtle.goto(x, y)
        t += 2*math.pi/n
    turtle.end_fill()


def RollingColumn(x, size):
    for y in range(-400, 500, 100):
        Ellipse(x, y, size, 35, 'white', 'black', 'dark orange')


def RollingColumn2(x, size):
    for y in range(-400, 500, 100):
        Ellipse(x, y, size, 35, 'black', 'white', 'dark orange')


def Rolling():
    RollingColumn(-450, 10)
    RollingColumn(-410, 13)
    RollingColumn(-360, 16)
    RollingColumn(-300, 19)
    RollingColumn(-240, 16)
    RollingColumn(-190, 13)
    RollingColumn(-150, 10)

    RollingColumn2(-130, 10)
    RollingColumn2(-90, 13)
    RollingColumn2(-40, 16)
    RollingColumn2(20, 19)
    RollingColumn2(80, 16)
    RollingColumn2(130, 13)
    RollingColumn2(170, 10)

    RollingColumn(190, 10)
    RollingColumn(230, 13)
    RollingColumn(280, 16)
    RollingColumn(340, 19)
    RollingColumn(400, 16)
    RollingColumn(450, 13)
    RollingColumn(490, 10)


turtle.color('steel blue')
turtle.up()
turtle.goto(-1000, -1000)
turtle.down()
turtle.begin_fill()
turtle.seth(0)
for _ in range(4):
    turtle.fd(2000)
    turtle.left(90)
turtle.end_fill()
turtle.pensize(3)
Rolling()
screen.update()
filename = "RollingIllusion.eps"
ts = turtle.getscreen()
ts.getcanvas().postscript(file=filename)
turtle.exitonclick()
