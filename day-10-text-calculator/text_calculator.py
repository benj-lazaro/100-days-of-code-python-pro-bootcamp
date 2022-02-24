
# Addition
def add(number1, number2):
    """Adds two numerical inputs & returns the sum."""
    return number1 + number2

# Subtraction
def subtract(number1, number2):
    """Subtracts two numerical inputs & returns the difference."""
    return number1 - number2

# Multiplication
def multiply(number1, number2):
    """Multiples two numerical inputs & returns the product."""
    return number1 * number2

# Division
def divide(number1, number2):
    """Divides two numerical inputs & returns the quotient."""
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:
    operation_symbol = input("Pick an operation: ")
    next_number = int(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, next_number)
    print(f"{num1} {operation_symbol} {next_number} = {answer}")

    user_response = input(f"Type 'y' to continue calaulating with {answer}, or type 'n' to exit.: ")

    if user_response == 'y':
        num1 = answer
    else:
        should_continue = False
