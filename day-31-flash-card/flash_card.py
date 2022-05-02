from tkinter import *
import pandas
import random

# Constant variable(s)
BACKGROUND_COLOR = "#B1DDC6"

# Global variable(s)
current_card = {}
to_learn = {}

try:
    # Read the CSV file on French words that the user has yet to learn based on previous session
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Read the following CSV if the app is run the first time
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Convert the CSV into a dictionary & stored as a list of dictionary items
    to_learn = data.to_dict(orient="records")


def next_card():
    """Pick a random French word from the imported CSV file"""
    global current_card, flip_timer

    # Cancel/reset the 3 seconds delay timer before picking a new French word
    window.after_cancel(flip_timer)

    # Pick & display a new French word
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Set a new 3 seconds delay timer
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Display the equivalent English word of the current French word"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """Remove the current French word from the list of dictionary items & save progress"""
    to_learn.remove(current_card)

    # Store French words that is yet to learn as a CSV file
    # Remove the unintended index number bug that gets appended to the CSV content at every iteration
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Set up the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a 3 seconds delay timer before displaying the English translation of the current French word
flip_timer = window.after(3000, func=flip_card)

# Set up the canvas
canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 153, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 264, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Set up the buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Load the 1st random French word from the imported CSV file
next_card()

window.mainloop()
