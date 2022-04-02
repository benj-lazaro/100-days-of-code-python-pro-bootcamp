from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        """Moves the turtle forward by the specified number of paces in MOVE_DISTANCE"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Moves the player back to the starting point"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Returns True if the current Y-axis reached beyond the finished line; otherwise return False"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
