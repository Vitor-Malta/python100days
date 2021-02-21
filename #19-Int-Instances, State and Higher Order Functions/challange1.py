from turtle import Turtle, Screen

# Event listener

diu = Turtle()
screen = Screen()

def move_forward():
    diu.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)



screen.exitonclick()
