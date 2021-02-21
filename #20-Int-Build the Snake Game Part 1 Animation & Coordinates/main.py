from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake_body = []
snake_position = [0, 20]  # initial position
for i in range(0, 3):
    snake_body.append(Turtle(shape="square",))
    snake_body[i].penup()
    snake_body[i].color("white")
    snake_body[i].goto(snake_position[0], (snake_position[1]))

    snake_position[0] -= 20


def move_forward():
    for index in range(0, len(snake_body)):
        snake_body[index].forward(10)


def move_backward():
    snake.backward(20)


def rotate_clockwise():
    snake.right(10)


def rotate_counter_clockwise():
    snake.left(10)


def clear_screen():
    screen.resetscreen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
