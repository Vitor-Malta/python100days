from turtle import Turtle, Screen
import time


def rotate(snake_seg, direction):
    if direction == "left":
        snake_seg.setheading(180)
    elif direction == "right":
        snake_seg.setheading(0)
    elif direction == "down":
        snake_seg.setheading(270)
    elif direction == "up":
        snake_seg.setheading(90)


def rotate_up():
    segments[0].setheading(90)
def rotate_down():
    segments[0].setheading(270)
def rotate_right():
    segments[0].setheading(0)
def rotate_left():
    segments[0].setheading(180)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)
screen.listen()


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments), 0, -1):
        seg_num -= 1
        if seg_num == 0:
            segments[seg_num].forward(20)
        else:
            next_seg_position = segments[seg_num - 1].pos()
            segments[seg_num].goto(next_seg_position)


