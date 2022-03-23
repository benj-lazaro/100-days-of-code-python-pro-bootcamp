from turtle import Turtle

# X-Y axis coordinates of 3-segment starter snake as tuples in a list
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # Reference to the head of the snake
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a 3-segment starter snake"""
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Moves the starter snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Moves the snake head forward at the specified distance / paces
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves the snake head up"""
        self.head.setheading(90)

    def down(self):
        """Moves the snake head down"""
        self.head.setheading(270)

    def left(self):
        """Moves the snake head to the left"""
        self.head.setheading(180)

    def right(self):
        """Moves the snake head to the right"""
        self.head.setheading(0)

