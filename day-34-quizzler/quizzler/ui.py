from tkinter import *
from quiz_brain import QuizBrain

# Constant Variable(s)
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Set up the Label widget
        self.score_label = Label(text="Score: 0")
        self.score_label.config(fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Set up the Canvass widget
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 19, "italic"))
        self.canvas.config(bg="white", highlightthickness=0)
        # Add 50px padding on the Y-axis to evenly space the top & bottom
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Set up the Buttons widgets
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true_pressed)
        self.true_button.grid(column=0, row=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false_pressed)
        self.false_button.grid(column=1, row=2, pady=20)

        # Load the question text into the canvas
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Fetch the question & route to the Canvass widget"""
        # Reset the Canvas widget's background color
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Prompt a message to the user & disable the buttons
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true_pressed(self):
        """True button clicked, verifies with quiz_brain's check_answer()"""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false_pressed(self):
        """False button clicked, verifies with quiz_brain's check_answer()"""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Provide visual feedback by changing Canvass widget background color"""
        if is_right:
            self.canvas.itemconfig(self.question_text, fill="black")
            self.canvas.config(bg="green")
        else:
            self.canvas.itemconfig(self.question_text, fill="black")
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
