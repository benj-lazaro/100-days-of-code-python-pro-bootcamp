# Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
end_of_game = False


# Testing code
print(f"Psst, the solution is {chosen_word}.")

# Create blanks
display = []

for position in range(chosen_word_length):
    display += "_"

# TODO #1: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blank ("_"). Then you can tell the user they've won.

while not end_of_game:
    guess = str(input("Guess a letter: ")).lower()

    # Check guessed letter
    for index_position in range(chosen_word_length):
        if guess == chosen_word[index_position]:
            display[index_position] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
