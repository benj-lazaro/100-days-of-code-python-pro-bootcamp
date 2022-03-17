from turtle import Turtle, Screen

# Instantiate an object from Turtle class
tim = Turtle()

# Draw the 100x100 square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
