
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

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]

# Bug: The 2nd operational_symbol will be used to calculate all 3 numbers
# The 1st operational_symbol will be disregarded
second_answer = calculation_function(calculation_function(num1, num2), num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
