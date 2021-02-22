from turtle import Screen
from time import sleep

class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(n=0)
        self.screen.listen()

    def run(self):
        while True:
            self.screen.update()
            sleep(0.1)
