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
    "/": divide
}

def calculator():
    user_next_move = True
    num1 = float(input("Enter first number: "))

    while user_next_move:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter your choice: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue to calculating with {answer} or type 'n' for new calculation: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            user_next_move = False
            print("\n" * 20)
            calculator()
        else:
            print("you enter the wrong value")
            print("\n" * 20)
            calculator()


calculator()