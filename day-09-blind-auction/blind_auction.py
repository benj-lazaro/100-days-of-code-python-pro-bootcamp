# Import art.py for program logo
from art import logo

# Global data structure & variable
bidders = {}
auction = True

# Mimic replit's clear() function
def clear_terminal_screen():
    print("\n" * 100)

# Determine the auction's winner (i.e. highest bidder)
def find_auction_winner(bidding_record):
    highest_bid = 0
    leading_bidder = ""

    for bidder in bidders:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            leading_bidder = bidder

    print(f"The winner is {leading_bidder} with a bid of ${highest_bid}.")

# Print logo & welcome message
print(logo)
print("Welcome to the secret auction program.")

# Gather data (name & bid value) & then determine the winnder
while auction:
    name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))
    bidders[name] = bid_value

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding  == 'yes':
        clear_terminal_screen()
    else:
        auction = False
        clear_terminal_screen()
        find_auction_winner(bidders)
