from game_data import data
from art import logo, vs
from random import randint


def clear():
    print("\n" * 130)
    return


def run():
    compare_a = data[randint(0, len(data) - 1)]
    compare_b = data[randint(0, len(data) - 1)]
    end_game = False
    user_score = 0
    while end_game == False:
        clear()
        print(logo)
        if user_score > 0:
            print(f"You are correct! Current score: {user_score}")
        print(f"\nCompare A : {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(f"{vs}")
        print(f"\nCompare B : {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        # print(compare_a["follower_count"], compare_b["follower_count"])
        user_answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        if compare_a["follower_count"] > compare_b["follower_count"]:
            answer = "a"
        else:
            answer = "b"
        if user_answer == answer:
            user_score += 1
            compare_a = compare_b.copy()
            compare_b = data[randint(0, len(data) - 1)]
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            end_game = True


run()
