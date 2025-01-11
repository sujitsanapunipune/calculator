# Simple Calculator in Python

# Function to add two numbers
def add(x, y):
    sum = x + y
    return print(f"Sum of {x} and {y} is {sum}")

# Function to subtract two numbers
def subtract(x, y):
    diff = x - y
    return print(f"Difference of {x} and {y} is {diff}")

def Multiplication(x, y):
    mult = x * y
    return print(f"Multiplication of {x} and {y} is {mult}")

def Division(x, y):
    div = x / y
    try:
        return print(f"division of {x} and {y} is {div}")
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed. Zero Division Error Occured"
    
def Modulus(x, y):
    mod = x % y
    try:
        return print(f"Modulus of {x} and {y} is {mod}")
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed. Zero Division Error Occured"


# Main function
def calculator():
    print("Simple Calculator. (My First Programme on GIT HUB)")
    print("Choose operation You want to Perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    # Take user input for operation
    choice = input("Enter choice (1 to 5): ")

    # Take user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation
    if choice == '1':
        add(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == "3":
        Multiplication(num1, num2)
    elif choice == "4":
        Division(num1, num2)
    elif choice == "5":
        Modulus(num1, num2)
    else:
        print("Invalid input. Please select a valid operation (1 OR 2 Or 3).")

# Run the calculator
calculator()