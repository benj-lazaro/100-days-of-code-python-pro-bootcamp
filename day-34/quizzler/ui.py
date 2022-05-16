from tkinter import *


# Constant Variable(s)
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Set up the Label widget
        self.label = Label(text="Score: 0")
        self.label.config(fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        # Set up the Canvass widget
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Set up the Buttons widgets
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2, pady=20)

        self.window.mainloop()
