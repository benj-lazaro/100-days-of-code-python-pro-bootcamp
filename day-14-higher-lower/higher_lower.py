from art import logo, vs
from game_data import data
from random import choice

def clear_screen_and_display_logo():
    """Clears the terminal screen"""
    print("\n" * 100)
    print(logo)

def compare_followers(item_1, item_2):
    """Takes two dictionary items and returns the one with a higher follower_count"""
    if item_1['follower_count'] > item_2['follower_count']:
        return item_1
    else:
        return item_2

def format_data(item):
    """Format dictionary item into a printable format"""
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

# Clear the terminal screen & display game logo
clear_screen_and_display_logo()

while not is_game_over:
    # Get random dictionary items from game_data
    if score == 0:
        item_1 = get_random_dictionary_item()
        item_2 = get_random_dictionary_item()
    else:
        item_2 = get_random_dictionary_item()

    # Check for duplicate entries
    if item_1 == item_2:
        item_2 = get_random_dictionary_item()

    # Identify which dictionary item has more follower_count
    correct_answer = compare_followers(item_1, item_2)

    # Display item's name, description & country
    print(f"Compare A: {format_data(item_1)}.")
    print(vs)
    print(f"Against B: {format_data(item_2)}.")

    # Ask for player's choice
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Evaluate player choice
    if player_choice == "A":
        selected_item = item_1
    else:
        selected_item = item_2

    # Check if player's choice is correct
    if correct_answer['name'] == selected_item['name']:
        # Increment player score & display feedback to player
        score += 1
        clear_screen_and_display_logo()
        print(f"\nYou are right. Current score: {score}\n")
        item_1 = correct_answer
    else:
        # Inform player got it wrong, display the score & end the game
        clear_screen_and_display_logo()
        print(f"\nSorry, that's wrong. Final score: {score}\n")
        is_game_over = True
