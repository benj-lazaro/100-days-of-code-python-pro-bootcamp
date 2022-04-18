# Layout manager using .place() layout manager
# CONS: Location specific; not good when managing multiple widgets

from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = input_field.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# Place the label at top-left corner of the screen
my_label.place(x=0, y=0)

# Button
button = Button(text="Click Me", command=button_clicked)


# Entry
input_field = Entry(width=10)


window.mainloop()
