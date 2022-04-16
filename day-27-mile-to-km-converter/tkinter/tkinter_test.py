from tkinter import *

# Instantiate Tk class to create a new window
window = Tk()

# Set the window's title
window.title("My First GUI Program")

# Scale the minimal window size to display the components included within the window
window.minsize(width=500, height=300)

# To add a label within a window
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# To change the text of a label
my_label["text"] = "New Text"

# Alternative way to change the text of a label
my_label.config(text="A Much Newer Text")


# Define a function for the button's event listener
def button_clicked():
    # Prints the following line on the console
    print("I got clicked!")

    # Returns the typed content on the entry component
    new_text = input_field.get()

    # Replaces the text of the label with the contents of the entry component
    my_label.config(text=new_text)


# To add a button w/ an event listener within a window
button = Button(text="Click Me", command=button_clicked)
button.pack()

# To add an entry component
input_field = Entry(width=10)
input_field.pack()

# Allows the window to remain open
window.mainloop()
