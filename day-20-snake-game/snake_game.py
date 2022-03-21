from turtle import Screen, Turtle

# Instantiate object from class Screen
screen = Screen()

# Setup screen as 600 pixels wide by 600 pixels high
screen.setup(width=600, height=600)

# Set screen background color to black and title to "My Snake Game"
screen.bgcolor("black")
screen.title("My Snake Game")

# X-Y axis coordinates of 3-segment starter snake
starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(position)

screen.exitonclick()
