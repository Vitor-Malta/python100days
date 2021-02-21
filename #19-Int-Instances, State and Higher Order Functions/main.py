# Turtle Race
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "gold", "green", "blue", "purple"]
turtles = []

x_position = -230
y_position = -120

# Turtles positioning
for x in range(0, len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[x].color(colors[x])
    turtles[x].penup()
    turtles[x].goto(x_position, y_position)
    y_position += 40

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: red, orange,"
                                                          " gold, green, blue or purple ")

# Turtles random move:
winner = ""
while not winner:
    for x in range(0, len(turtles)):
        turtles[x].forward(randint(0,6))
        if turtles[x].pos()[0] >= 225:
            winner = turtles[x].color()[0]
print(f"The winner was {winner}")
if winner == user_bet:
    print("Congratulations you win!")
else:
    print("Try again, maybe next time you'll win.")
screen.exitonclick()
