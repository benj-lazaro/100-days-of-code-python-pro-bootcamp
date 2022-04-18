# Layout manager using .grid() layout manager
# NOTE: Start with the widget that you want at the top (0,0)
# Then for the next subsequent widgets & keep through it

from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = input_field.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Insert padding (i.e. space) on the X & Y axis of the window
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# Label will be placed at the column 0 and row 0
my_label.grid(column=0, row=0)
# Insert padding (i.e. space) on the X & Y axis on the Label widget
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
# Button will be placed at the column 1 and row 1
button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button", command=button_clicked)
# New button will be placed at column 2 and row 0
new_button.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
# Label will be placed at the column 2 and row 2
input_field.grid(column=3, row=2)


window.mainloop()
