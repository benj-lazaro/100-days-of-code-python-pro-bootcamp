# The Official Rules of Rock, Paper, Scisors (https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)
# Three (3) Simple Rules
# 1. Rock wins against Scissors
# 2. Scissors wins against Paper
# 3. Paper wins against Rock

# ASCII hand gestures
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Import random module
import random

# Store hand gesture choices to a list; accessed via index value
hand_gesture = [rock, paper, scissors]

# Display game rules and get user's choices
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Generate program's choice using the random module's randint() method & passing values between 0 to 2
computer_choice = random.randint(0, 2)

# Compare computer's and user's choices
if (user_choice >= 3) or (user_choice < 0):
    print("You typed an invalid number, you lose!")
# Rock wins over Scissors
elif (user_choice == 0) and (computer_choice == 2):
    print(hand_gesture[user_choice])
    print("Computer choose:")
    print(hand_gesture[computer_choice])
    print("You win.")
# Scissors wins over Paper
elif (user_choice == 2) and (computer_choice == 1):
    print(hand_gesture[user_choice])
    print("Computer choose:")
    print(hand_gesture[computer_choice])
    print("You win.")
# Paper wins over Rock
elif (user_choice == 1) and (computer_choice == 0):
    print(hand_gesture[user_choice])
    print("Computer choose:")
    print(hand_gesture[computer_choice])
    print("You win.")
# A draw
elif user_choice == computer_choice:
    print(hand_gesture[user_choice])
    print("Computer choose:")
    print(hand_gesture[computer_choice])
    print("It is a draw.")
# User loses
else:
    print(hand_gesture[user_choice])
    print("Computer choose:")
    print(hand_gesture[computer_choice])
    print("You lose.")
