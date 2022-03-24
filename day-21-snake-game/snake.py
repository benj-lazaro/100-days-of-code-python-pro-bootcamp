from turtle import Turtle

# X-Y axis coordinates of 3-segment starter snake as tuples in a list
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Snake movements
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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

    # Defines the methods of arrow-key movement control of the snake
    # Prevent the keys from going back on itself
    def up(self):
        """Moves the snake head up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake head down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake head to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake head to the right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
