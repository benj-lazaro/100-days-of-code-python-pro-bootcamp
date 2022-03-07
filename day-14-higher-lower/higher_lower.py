from art import logo, vs
from game_data import data
from random import choice

def check_answer(guess, item_1, item2):
    """Take two dictionary items and returns the correct answer"""
    if item_1['follower_count'] > item_2['follower_count']:
        return guess == "A"
    else:
        return guess == "B"

def clear_screen_and_display_logo():
    """Clears the terminal screen"""
    print("\n" * 100)
    print(logo)

def format_data(item):
    """Takes a dictionary item and return a printable format"""
    name = item['name']
    description = item['description']
    country = item['country']
    return f"{name}, a {description}, from{country}"

def get_random_dictionary_item():
    """Returns random dictionary items from game_data module"""
    return choice(data)

# Global variables
score = 0
is_game_over = False

# Initially get random dictionary item from game data
item_2 = get_random_dictionary_item()

# Clear the terminal screen & display game logo
clear_screen_and_display_logo()

while not is_game_over:
    # Set dictionary item for item_2 to item_1 & get a new one for item_2
    item_1 = item_2
    item_2 = get_random_dictionary_item()

    # Check for duplicate dictionary items
    while item_1 == item_2:
        item_2 = get_random_dictionary_item()

    # Display dictionary items' name, description & country
    print(f"Compare A: {format_data(item_1)}.")
    print(vs)
    print(f"Against B: {format_data(item_2)}.")

    # Ask for player's choice
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Verify player's choice
    is_player_correct = check_answer(player_choice, item_1, item_2)

    clear_screen_and_display_logo()
    if is_player_correct:
        # Increment player score & display feedback to player
        score += 1
        print(f"\nYou are right. Current score: {score}\n")
    else:
        # Inform player got it wrong, display the score & end the game
        is_game_over = True
        print(f"\nSorry, that's wrong. Final score: {score}\n")
