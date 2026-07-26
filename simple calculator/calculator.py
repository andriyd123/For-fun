from art import calculator_art

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

def calculator():
    print(calculator_art)

    number1 = float(input("What's the first number?: "))

    keep_running = True

    while keep_running:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        if operation in operations:
            number2 = float(input("What's the next number?: "))
            answer = operations[operation](number1, number2)
            print(f"{number1} {operation} {number2} = {answer}")
            continue_working = input(f"Type 'y' to continue working with {answer}, or type 'n' to start a new calculation: ").lower()
            if continue_working == 'y':
                number1 = answer
            else:
                keep_running = False
                print("\n" * 100)
                calculator()
        else:
            print("Invalid operation, please try again.")
            calculator()

calculator()

