def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

while True:
    # Display menu
    print("Options:")
    print("Enter 'addition' for addition")
    print("Enter 'subtraction' for subtraction")
    print("Enter 'multiplication' for multiplication")
    print("Enter 'division' for division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("addition", "subtraction", "multiplication", "division"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "addition":
            print("Result:", addition(num1, num2))
        elif user_input == "subtraction":
            print("Result:", subtraction(num1, num2))
        elif user_input == "multiplication":
            print("Result:", multiplication(num1, num2))
        elif user_input == "division":
            print("Result:", division(num1, num2))
    else:
        print("Invalid input. Please enter a valid option.")