from turtle import Turtle

# Constant variables
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        # Relocate scoreboard at the following coordinates
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes the scoreboard on screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increments the score by 1"""
        self.score += 1
        # Clear the previous text (score) from the screen
        self.clear()
        self.update_scoreboard()

