from game_data import data
from art import logo, vs
from random import randint


def clear():
    print("\n"*130)


def run_higher_lower():
    print(logo)
    user_score += compare()

    return


def compare():
    compare_a = data[randint(0, len(data) - 1)]
    compare_b = data[randint(0, len(data) - 1)]
    end_game = False
    while not end_game:
        print("nda")


run_higher_lower()
