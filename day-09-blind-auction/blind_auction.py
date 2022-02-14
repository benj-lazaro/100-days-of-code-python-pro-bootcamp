# Import art.py for program logo
from art import logo

# Global data structure & variable
bidders = {}
auction = True

# Mimic replit's clear() function
def clear_terminal_screen():
    print("\n" * 100)

# Determine the auction's winner (i.e. highest bidder)
def auction_winner():
    highest_bid = 0
    highest_bidder = ""

    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bidder = key
            highest_bid = bidders[key]

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# Print logo & welcome message
print(logo)
print("Welcome to the secret auction program.")

# Gather data (name & bid value) & then determine the winnder
while auction:
    name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))
    bidders[name] = bid_value

    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_auction == 'yes':
        clear_terminal_screen()
    else:
        auction = False
        clear_terminal_screen()
        auction_winner()
