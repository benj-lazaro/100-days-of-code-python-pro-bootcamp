# Import random module
import random

# List of lowercae & uppercase letters, numbers & symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display greetings
print("Welcome to the PyPassword Generator!")

# Ask user how many letters, symbols & numbers to be included in the password
password_letters = int(input("How many letters would you like in your password? "))
password_symbols = int(input("How many symbols would you like? "))
password_numbers = int(input("How many numbers? "))

password_generated = ""
# Easy level: Generate password in sequence order (letter, symbol & number)
for character in range(1, password_letters + 1):
    password_generated += random.choice(letters)

for symbol in range(1, password_symbols + 1):
    password_generated += random.choice(symbols)

for number in range(1, password_numbers + 1):
    password_generated += random.choice(numbers)

# Display generated password
print(f"Easy Level Password: {password_generated}")

# Hard level: Generate password in completely random order
hard_password_generated = ""

for character in password_generated:
    hard_password_generated += random.choice(password_generated)

print(f"Hard Level Pasword:  {hard_password_generated}")
