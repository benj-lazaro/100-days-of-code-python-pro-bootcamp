from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Save and append user entry into a text file"""
    # Fetch data from entry widgets
    website_data = website_entry.get()
    email_username_data = email_username_entry.get()
    password_data = password_entry.get()

    # Check for empty fields
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave fields empty!")
    else:
        # Show a message box to verify data to be saved
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \n "
                                                                   f"Email: {email_username_data} \n "
                                                                   f"Password: {password_data} \n"
                                                                   f"Is it ok to save?")

        if is_ok:
            # Format collected data
            data_entry = f"{website_data} | {email_username_data} | {password_data}\n"

            # Append & write formatted data to the file data.txt
            with open("data.txt", mode="a") as data_file:
                data_file.write(data_entry)
                # Clear the entry widgets except for the username/email
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                # Refocus cursor back to the website entry widget
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
generate_password_button = Button(text="Generate", width=5, pady=0)
generate_password_button.grid(column=2, row=3)

add_user_entry_button = Button(text="Add", width=32, pady=0, command=save)
add_user_entry_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
