from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input(f"What would you like? ({menu.get_items()[:-1]}) ")
    if order in menu.get_items():
        user_coffee = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(user_coffee):
            if money_machine.make_payment(user_coffee.cost):
                coffee_maker.make_coffee(user_coffee)
    elif order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print("Invalid input, try again.")
