# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# MAZE
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and not right_is_clear():
        move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
