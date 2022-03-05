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

def get_random_item():
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
        item_1 = get_random_item()
        item_2 = get_random_item()
    else:
        item_2 = get_random_item()

    # Identify which item has greater follower_count
    correct_answer = compare_followers(item_1, item_2)

    # Display item's name, description & country
    print(f"Compare A: {item_1['name']}, a {item_1['description']}, from {item_1['country']} ")
    print(vs)
    print(f"Against B: {item_2['name']}, a {item_2['description']}, from {item_2['country']} ")

    # Ask for player's choice
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if player_choice == "A":
        selected_item = item_1
    else:
        selected_item = item_2

    # Check player's choice
    if correct_answer['name'] == selected_item['name']:
        # Increment score by 1
        score += 1
        clear_screen_and_display_logo()
        print(f"\nYou are right. Current score: {score}\n")
        item_1 = correct_answer
    else:
        # Game over, man!
        clear_screen_and_display_logo()
        print(f"\nSorry, that's wrong. Final score: {score}\n")
        is_game_over = True
