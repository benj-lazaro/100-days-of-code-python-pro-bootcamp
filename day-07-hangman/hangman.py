import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

# Testing code
# print(f"Psst, the solution is {chosen_word}.")

# Create blanks
display = []

for position in range(chosen_word_length):
    display += "_"

while not end_of_game:
    guess = str(input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index_position in range(chosen_word_length):
        letter = chosen_word[index_position]

        if letter == guess:
            display[index_position] = guess

    if guess not in chosen_word:
        print(f"You have guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
