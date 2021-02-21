from random import randint


def guessing_number_game():
    print("Welcome to the Guessing Number Game!!!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose difficulty 'easy' or 'hard': ")
    while True:
        if difficulty == "easy":
            lives = 10
            break
        elif difficulty == "hard":
            lives = 5
            break
        else:
            difficulty = input("Please, choose difficulty between 'easy' or 'hard': ")
    answer = randint(1, 100)
    print(f"Pss the answer is '{answer}'...")

    while lives > 0 and user_answer != answer:
        user_answer = int(input("Make a guess: "))
        if user_answer != answer:
            if user_answer > answer:
                print(f"Too high, you lost a live. You have {lives - 1} left.")
            elif user_answer < answer:
                print(f"Too low, you lost a live. You have {lives - 1} left.")
            lives -= 1
    if lives == 0:
        print(f"You are out of lives, maybe next time you can win.\nThe answer was {answer}. ")
    elif user_answer == answer:
        print(f'You win! {user_answer} is the correct answer, you had {lives} left. Good job!')


guessing_number_game()
