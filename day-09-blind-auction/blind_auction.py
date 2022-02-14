# Import art.py for program logo
from art import logo

# Global data structure
bidders = {}

# Global variables
auction = True
highest_bid = 0
highest_bidder = ""

# Mimic replit's clear() function
def clear_terminal_screen():
    print("\n" * 100)

# Print logo & welcome message
print(logo)
print("Welcome to the secret auction program.")

# Gather bidder name & bid value
while auction:
    name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))
    bidders[name] = bid_value

    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if others == 'yes':
        clear_terminal_screen()
    else:
        auction = False
        clear_terminal_screen()

# Determine the auction's winner (i.e. highest bidder)
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bidder = key
        highest_bid = bidders[key]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
