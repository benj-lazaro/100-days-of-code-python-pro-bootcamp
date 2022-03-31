from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        """Moves the ball to the top-right corner of the screen by 10 pixels at a time"""
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

