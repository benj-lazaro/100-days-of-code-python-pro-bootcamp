from tkinter import *


def miles_to_km():
    # Convert input value from string to float
    miles = float(miles_input.get())
    # Covert miles to kilometers; round the value to a whole number
    km = round(miles * 1.609)
    # Convert the value back to string & update the text of the corresponding label
    km_result_label.config(text=f"{km}")


# Create the window with a padding of 20px on both X & Y axis
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Create an Entry widget & place within the window
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.focus()

# Create Label widgets & place within the window
miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label()
is_equal_to_label.config(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label()
km_result_label.config(text="0")
km_result_label.grid(column=1, row=1)

kilometer_label = Label()
kilometer_label.config(text="Km")
kilometer_label.grid(column=2, row=1)

# Create a button widget & place within the window
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Keep the window open until manually closed
window.mainloop()
