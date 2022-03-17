import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205),
              (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176),
              (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108),
              (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98),
              (215, 184, 172), (190, 190, 195), (78, 72, 31)]

# Set the speed of cursor
tim.speed("fastest")

# Hide the turtle cursor path from showing on the screen
tim.penup()

# Hide the turtle cusor
tim.hideturtle()

# Adjust turtle cursor to face angle 255
tim.setheading(225)

# Move the cursor 250 paces from its current position
tim.forward(350)

# Reset heading of cursor to 0 in order to start from bottom-left of the screen
tim.setheading(0)

number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()