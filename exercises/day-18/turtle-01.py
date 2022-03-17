from turtle import Turtle, Screen

# Instantiate an object from Turtle class
timmy_the_turtle = Turtle()

# Set the shape of the turtle cursor to "turtle"
timmy_the_turtle.shape("turtle")

# Set the color of the turtle cursor to red
# Colors are based on the Tk color specification string
# Source (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html)
timmy_the_turtle.color("red")

# Move the turtle cursor forward of 100 paces / steps
timmy_the_turtle.forward(100)

# Move the turtle cursor right at 90 degrees from its current position
timmy_the_turtle.right(90)

# Instantiate an object from Screen class
screen = Screen()

# Call the method that displays the window & exits only when clicked
screen.exitonclick()
