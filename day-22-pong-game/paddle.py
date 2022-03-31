from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def up(self):
        """Moves the paddle up by 20 paces"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddle down by 20 paces"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
