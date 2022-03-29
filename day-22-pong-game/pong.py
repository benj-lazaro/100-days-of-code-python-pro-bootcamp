from turtle import Screen

# Create a screen with black background color & a dimension of 800x600
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# Terminates the screen when clicked
screen.exitonclick()
