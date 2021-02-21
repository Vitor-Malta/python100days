import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
player_move = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

if player_move >=3 or player_move < 0:
    print("Invalid number, you lose.")
else:
    player_move = choices[int(player_move)]
    pc_move = choices[random.randint(0, 2)]
    print(f'\n{player_move}\n\n')

    print("Computer choose: ")

    result = ""
    print(f'\n{pc_move}\n\n')
    if player_move == rock:
        if pc_move == rock:
            result = "Draw"
        elif pc_move == paper:
            result = "You lose"
        elif pc_move == scissors:
            result = "You won"

    if player_move == paper:
        if pc_move == rock:
            result = "You won"
        elif pc_move == paper:
            result  = "Draw"
        elif pc_move == scissors:
            result = "You lose"

    if player_move == scissors:
        if pc_move == rock:
            result = "You lose"
        if pc_move == paper:
            result = "You win"
        if pc_move == scissors:
            result = "draw"
    print(result)

