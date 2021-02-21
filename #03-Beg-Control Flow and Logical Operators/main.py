# Treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision1 = input('You are on a cross road. Where do you want to go? Type "left" or "right".')
if decision1 == "left":
    decision2 = input('\nYou see a island in the middle of a lake. Do you want to wait for a boat or you want to \n'
                      'swim to the island? Type "wait" or "swim".')
    if decision2 == "wait":
        decision3 = input('\nYou arrive at the island unharmed. There is a house with 3 doors at your front.\n'
                          'A yellow door, a blue door and a red door.\n'
                          'Which door do you want to open? The "red", "blue" or the "yellow" one?')
        if decision3 == "blue":
            print("GAME OVER. You have been eaten by beasts.")
        elif decision3 == "red":
            print("GAME OVER. You have been burned by fire.")
        elif decision3 == "yellow":
            print("You won! You have found the treasure chest. Congratulations!!!")
        else:
            print("GAME OVER")
    else:
        print("Attacked by trout. GAME OVER")

else:
    print("You are dead. You fell at a hole, GAME OVER.")