# Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Psst, the solution is {chosen_word}.")

# TODO #1: Create an empty list called display.
# For each letter in the chosen_word, add "_" to 'display'
# SO if the chosen_word is 'apple', display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
chosen_word_length = len(chosen_word)

for position in range(chosen_word_length):
    display += "_"

guess = str(input("Guess a letter: ")).lower()

# TODO #2: Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen_word was "apple", then display should be ["_", "p", "p", "_", "_"]
# for character in chosen_word:
#     if character == guess:
#         print("Right")
#         print(character)
#     else:
#         print("Wrong")

for index_position in range(chosen_word_length):
    if guess == chosen_word[index_position]:
        display[index_position] = guess

# TODO #3: Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
# Hint - Don't worry about getting the user to guess the next leter. We'll tackle that in step 3.
print(display)
