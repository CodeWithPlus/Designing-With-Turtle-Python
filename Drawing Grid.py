from turtle import Screen, Turtle

GRID_SIZE = 600

sub_divisions = 33

cell_size = GRID_SIZE / float(sub_divisions)

screen = Screen()
screen.title = "Drawing Grid by MuhammadShahsawar"

turtle = Turtle()
turtle.penup()
turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
turtle.pendown()

angle = 90

for _ in range(4):
    turtle.forward(GRID_SIZE)
    turtle.right(angle)

for _ in range(2):
    for _ in range(1, sub_divisions):
        turtle.forward(cell_size)
        turtle.right(angle)
        turtle.forward(GRID_SIZE)
        turtle.left(angle)

        angle = -angle

    turtle.forward(cell_size)
    turtle.right(angle)

screen.exitonclick()
