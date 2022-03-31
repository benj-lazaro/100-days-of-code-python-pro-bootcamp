from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball to the top-right corner of the screen by 10 pixels at a time"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Moves the ball to its  reverse direction along the y-axis"""
        self.y_move *= -1

    def bounce_x(self):
        """Moves the ball to its reverse direction along the x-axis"""
        self.x_move *= -1

    def reset_position(self):
        """Resets the position of the ball back to its initial state"""
        self.goto(0, 0)
        self.bounce_x()
