from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # Opens data.txt file & read the current high score
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and update the scoreboard with the latest score"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the scoreboard & (if applicable) writes the new high score"""
        if self.score > self.high_score:
            self.high_score = self.score

            # Open the data.txt file & writes the new high score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        # Resets the current score back to 0 & update the scoreboard
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increments the current score by 1"""
        self.score += 1
        self.update_scoreboard()
