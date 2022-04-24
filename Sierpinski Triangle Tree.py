import turtle
turtle.title('Sierpinski Tree by MuhammadShahsawar')
turtle.setworldcoordinates(-2000, -2000, 2000, 2000)
screen = turtle.Screen()
screen.tracer(0, 0)
turtle.hideturtle()


def SierpinskiTree(x, y, length, tilt, n):
    if n == 0:
        return
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(tilt)
    turtle.down()
    turtle.fd(length)
    SierpinskiTree(turtle.xcor(), turtle.ycor(),
                    length/2, turtle.heading(), n-1)

    turtle.up()
    turtle.goto(x, y)
    turtle.seth(tilt+120)
    turtle.down()
    turtle.fd(length)
    SierpinskiTree(turtle.xcor(), turtle.ycor(),
                    length/2, turtle.heading(), n-1)

    turtle.up()
    turtle.goto(x, y)
    turtle.seth(tilt-120)
    turtle.down()
    turtle.fd(length)
    SierpinskiTree(turtle.xcor(), turtle.ycor(),
                    length/2, turtle.heading(), n-1)


SierpinskiTree(0, -250, 1000, 90, 8)
screen.update()
screen.exitonclick()
