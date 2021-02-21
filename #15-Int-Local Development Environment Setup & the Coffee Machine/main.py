MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def run_coffee_machine(starting_resources):
    """
     Run the machine
     args: starting_resources - to get and update the resources
    """
    current_machine_resources = resources.copy()
    while True:
        successful_request = False
        while not successful_request:
            user_request = get_user_request(current_machine_resources)
            if user_request == "off":
                return
            successful_request = insert_coins(user_request)
            if successful_request:
                ingredients = MENU[user_request]["ingredients"]
                for key in ingredients:
                    current_machine_resources[key] -= ingredients[key]
                current_machine_resources["money"] += MENU[user_request]["cost"]
                print(current_machine_resources)


def get_user_request(current_resources):
    while True:
        user_coffee_choice = input("\nWhat would you like? (espresso/latte/cappuccino) ")
        if user_coffee_choice == "off":
            return "off"
        elif user_coffee_choice == "report":
            print(f"Water: {current_resources['water']}ml"
                  f"\nMilk: {current_resources['milk']}ml"
                  f"\nCoffee: {current_resources['coffee']}g"
                  f"\nMoney: R$ {current_resources['money']:.2f}")
        elif user_coffee_choice == "espresso" or user_coffee_choice == "latte" or user_coffee_choice == "cappuccino":
            if check_resources(request=user_coffee_choice, current_resources2=current_resources):
                return user_coffee_choice
        else:
            print("Invalid input, please try again.")


def check_resources(request, current_resources2):
    ingredients = MENU[request]["ingredients"]
    for key in ingredients:
        if ingredients[key] > current_resources2[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def insert_coins(request):
    coffee_cost = MENU[request]["cost"]
    print(f"The cost of {request} is R$ {coffee_cost:.2f}, please insert coins.")
    quarters = int(input("How many quarters? ($0.25) ")) * 0.25
    dimes = int(input("How many dimes? ($0.10) ")) * 0.10
    nickles = int(input("How many nickles? ($0.05)")) * 0.05
    pennies = int(input("How many pennies? ($0.01)")) * 0.01
    inserted_coins_total = quarters + dimes + nickles + pennies
    print(f"Total of money inserted: R$ {inserted_coins_total:.2f}.")
    return check_coins(inserted_coins=inserted_coins_total, request_cost=coffee_cost, coffee=request)


def check_coins(inserted_coins, request_cost, coffee):
    if inserted_coins >= request_cost:
        print(f"Thank you! Please wait a moment for you {coffee}.")
        if inserted_coins > request_cost:
            print(f"Here is your change: R$ {(inserted_coins - request_cost):.2f}")
        return True
    elif inserted_coins < request_cost:
        print(f"Not enough coins, money refunded.")


run_coffee_machine(resources)
