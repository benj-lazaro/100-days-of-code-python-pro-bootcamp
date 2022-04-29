from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Use list comprehension to shorten the code
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine the 3 lists into a single list
    password_list = password_letters + password_symbols + password_numbers
    # Randomize list items by shuffling
    shuffle(password_list)
    # Join randomize list items together using .join()
    password = "".join(password_list)
    # Clears previously generated password to prevent from generating a long one (optional)
    password_entry.delete(0, END)
    # Updates the password Entry widget with the generated password
    password_entry.insert(0, password)
    # Copy generated password in the host OS clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save and append user entry into a text file"""
    # Fetch data from entry widgets
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # Format of the JSON data file
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave fields empty!")
    else:
        # Write new entry to a JSON file
        with open("data.json", "r") as data_file:
            # Load old data from the JSON file & store it in a variable as a dictionary
            data = json.load(data_file)
            # Update the contents of the dictionary by appending the new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # Save / write the changes into the JSON file
            json.dump(data, data_file, indent=4)

            # Clear the widget fields & refocus cursor back to the Website: Entry widget
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# Setup window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Setup canvas widget
canvas = Canvas(width=200, height=200, highlightthickness=0)
# Load the background image into the canvas widget
logo_img = PhotoImage(file="logo.png")
canvas.create_image(85, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label widgets
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry widgets
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
# END = constant that places the cursor at the end of the inserted text
# 0 = a constant that places the cursor at the beginning of the inserted text
email_username_entry.insert(0, "email@test.com")

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

# Button widgets
generate_password_button = Button(text="Generate", width=5, pady=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_user_entry_button = Button(text="Add", width=32, pady=0, command=save)
add_user_entry_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
