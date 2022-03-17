from turtle import Turtle, Screen

# Instantiate an object from Turtle class
tim = Turtle()

# Draws a line for 10 paces with 10 gaps in-between (i.e. dashed line)
for _ in range(15):
    # Place the pen down & draw a line for 5 paces
    tim.pendown()
    tim.forward(10)

    # Pulls the pen up & draw a blank for 5 paces
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
