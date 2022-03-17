import turtle as t
import random


def draw_spirograph(size_of_gap):
    """Draws a spriograph"""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)

        # Shift the current heading by 10 degrees
        tim.setheading(tim.heading() + size_of_gap)

def random_color():
    """Returns a random RGB value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Instantiage object from class Turtle
tim = t.Turtle()

# Set the Turtle module's color mode to 255
t.colormode(255)

# Set drawing speed to fastest
tim.speed("fastest")

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
