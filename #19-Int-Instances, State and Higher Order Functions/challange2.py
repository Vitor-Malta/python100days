from turtle import Screen, Turtle


def move_forward():
    diu.forward(10)


def move_backward():
    diu.backward(10)


def rotate_clockwise():
    diu.right(10)


def rotate_counter_clockwise():
    diu.left(10)


def clear_screen():
    screen.resetscreen()
    pass


diu = Turtle()
screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
