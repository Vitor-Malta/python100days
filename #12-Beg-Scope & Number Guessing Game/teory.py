# Scope
def game():
    player_health = 100  # Local scope, cannot be accessed within another function.

    def drink_potion():
        potion_strength = 10
        print(f"The player health was {player_health} before the potion.")
        return potion_strength

    player_health += drink_potion()  # to modify a global scope using a function
    print(player_health)


game()
