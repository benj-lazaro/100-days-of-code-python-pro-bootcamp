# Draws a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon and decagon
# --------------------
# Each shape is drawn with a random color
# Each side is 100 paces in terms of length
# --------------------
# Each shape overlays on each other in sequence

import turtle as t
import random
# from turtle import Turtle, Screen
# from random import choice, randint


def random_color():
    """Returns a random RGB value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def random_walk(direction, color):
    """Takes two values (angle & color) and draws a line on the window"""
    tim.setheading(direction)
    tim.color(color)
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(20)


# Instantiage object from class Turtle
tim = t.Turtle()

# Set the Turtle module's color mode to 255
t.colormode(255)

# Define angles of direction (N, S, E, W)
angle = [0, 90, 180, 270]

# Define number of iterations
ITERATION = 301

for _ in range(ITERATION):
    # Select random angle of direction
    random_direction = random.choice(angle)

    # Perofrm random walk
    random_walk(random_direction, random_color())

screen = t.Screen()
screen.exitonclick()
