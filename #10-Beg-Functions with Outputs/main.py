from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}


def run_calculator():
    num1 = int(input("What's the first number?: "))

    for key in operations:
        print(key)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = int(input("What's the second number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"n1= {num1}, operator= {operation_symbol}, num2= {num2}, answer= {answer}")
    continue_calculator = input("Do you want to continue calculating? Type 'y' for yes or 'n' for no.")
    if continue_calculator.lower() == 'n':
        return
    else:
        run_calculator_again(answer)


def run_calculator_again(calculator1_answer):
    continue_calculator = ""
    while continue_calculator != "n":
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the line above: ")
        num3 = int(input("What's the next number you want to calculate? "))
        answer = operations[operation_symbol](calculator1_answer, num3)
        print(
            f"Answer was = {calculator1_answer}, operator= {operation_symbol}, "
            f"new number to calculate= {num3}, new answer= {answer}")
        continue_calculator = input("Do you want to continue calculating? Type 'y' for yes or 'n' for no.")
        calculator1_answer = answer


run_calculator()
