from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

# Button widgets
generate_password_button = Button(text="Generate", width=5, pady=0)
generate_password_button.grid(column=2, row=3)

add_user_entry_button = Button(text="Add", width=32, pady=0)
add_user_entry_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
