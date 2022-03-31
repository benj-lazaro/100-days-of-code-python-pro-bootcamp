from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Display & updates the scoreboard"""
        self.clear()

        # Display left paddle player score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

        # Display right paddle player score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        """Increment left paddle player's score by 1"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increment right paddle player's score by 1"""
        self.r_score += 1
        self.update_scoreboard()
