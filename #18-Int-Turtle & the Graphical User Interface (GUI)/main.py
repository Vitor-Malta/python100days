import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice, randint

colors_pallet = colorgram.extract("hirst-paint.jpg", 15)

diu = Turtle()

diu.width(10)
diu.speed("fastest")
diu.penup()
directions = [0, 90, 180, 270]
screen = Screen()
turtle.colormode(255)


def hirst_paint(colors):
    for z in range(-100,200,20):
        diu.goto(-200,z)
        for i in range(0, 10):
            diu.dot(15, colors[randint(5,14)].rgb)
            diu.forward(30)


def circle_t():
    while True:
        diu.circle(50)
        diu.right(10)
        random_color()


def random_color():
    diu.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))


def random_walk():
    move_direction = choice(directions)  # select a random direction to the turtle move
    diu.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    diu.setheading(move_direction)  # face the random direction
    diu.forward(20)


hirst_paint(colors_pallet)

screen.exitonclick()
