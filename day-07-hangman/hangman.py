# Import module
import random

# Pre-made word list
word_list = ["ardvark", "baboon", "camel"]

# TODO #1: Randomly choose a word from the word_list and assign it to a variable called chosen_word
random_index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[random_index]

# TODO #2: Ask the user to guess a letter and assign their answer to a variable called guess.
# Make the value of guess lowercase.
guess = str(input("Guess a letter: ")).lower()

# TODO #3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word
for character in range(0, len(chosen_word)):
    if (chosen_word[character] == guess):
        print("Right")
    else:
        print("Wrong")
