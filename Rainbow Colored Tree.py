import turtle
import colorsys


def DrawStick(x, y, length, pensize, color, angle):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(angle)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.fd(length)


def DrawTree(x, y, length, pensize, hue, angle, fat_angle, n):
    if n == 0:
        return
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
    DrawStick(x, y, length, pensize, (r, g, b), angle)
    tx = turtle.xcor()
    ty = turtle.ycor()

    DrawTree(tx, ty, length*0.7, pensize*0.7, hue -
             1/13, angle+fat_angle, fat_angle, n-1)
    DrawTree(tx, ty, length*0.7, pensize*0.7, hue -
             1/13, angle-fat_angle, fat_angle, n-1)


turtle.setup(800, 800)
turtle.title("Rainbow Colored Tree by MuhammadShahsawar")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)
turtle.bgcolor('black')

DrawTree(0, -300, 200, 10, 12/13, 90, 25, 12)
turtle.update()
turtle.exitonclick()
