from turtle import Turtle, Screen
from time import sleep

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


class Snake:
    def __init__(self):
        self.body = segments
        self.head = segments[0]
        self.is_on = True

    def move(self):
        while True:
            for seg_number in range(len(segments), 0, -1):
                self.head.forward(20)
                next_seg_position = segments[seg_number - 1].pos()
                segments[seg_number].goto(next_seg_position)


snake = Snake()
