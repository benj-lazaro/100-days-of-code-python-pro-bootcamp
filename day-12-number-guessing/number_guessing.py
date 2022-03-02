#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

number_of_turns = 0
is_game_over = False

def clear_screen_terminal():
    """Clears the terminal screen."""
    print("\n" * 100)

def check_answer(user_guess, answer):
    """Takes in two integers, compare the values & return corresponding feedback"""
    if user_guess > answer:
        return "Too high."
    elif user_guess < answer:
        return "Too low."
    else:
        return 0

def set_game_level(level):
    """Takes in a string and returns the number of allowed guesses"""
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

clear_screen_terminal()

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")

# Generate random number between 1 and 100
answer = randint(1, 100)

# Get preference on game difficulty level
difficulty_level = str(input("Choose a difficulty level. Type 'easy' or 'hard': "))

number_of_turns = set_game_level(difficulty_level)
print(f"\nYou will have {number_of_turns} attempts remaining to guess the number.")

# Play the game
while not is_game_over:
    user_guess = int(input("Make a guess: "))
    result = check_answer(user_guess, answer)

    if result == 0:
        is_game_over = True
        print(f"You got it! The answer is {answer}.")
    else:
        print(result)

    number_of_turns -= 1

    if number_of_turns == 0:
        is_game_over = True
        print("You've run out of guesses, you lose.")
    elif number_of_turns != 0 and not is_game_over:
        print(f"You have {number_of_turns} attempts remaining to guess the number.")
