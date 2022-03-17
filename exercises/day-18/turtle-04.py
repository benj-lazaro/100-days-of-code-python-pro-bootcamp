# Draws a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon and decagon
# --------------------
# Each shape is drawn with a random color
# Each side is 100 paces in terms of length
# --------------------
# Each shape overlays on each other in sequence

from turtle import Turtle, Screen
from random import choice

tim = Turtle()

def draw_shape(sides, color):
    """Accepts two values and draws the corresponding shape"""
    # Set pre-determine length of each side
    line_length = 100

    # Calculate the angle value for each corresponding polygon
    angle = 360 / sides

    # Draw the polygon according to angle, color & number of sides
    for _ in range(sides):
        tim.color(color)
        tim.forward(line_length)
        tim.left(angle)


# Draw a 3-side up to 10-side polygon; each overlays over each other
for polygon in range(3, 11):
    color_palette = ["red", "blue", "green", "brown", "orange", "pink",
        "purple", "yellow", "fuchsia"]
    random_color = choice(color_palette)

    draw_shape(polygon, random_color)

screen = Screen()
screen.exitonclick()
