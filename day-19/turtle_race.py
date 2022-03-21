from turtle import Turtle, Screen
import random

# Instantiate object from Screen class
screen = Screen()

# Sets the screen dimension to 500 pixels wide and 400 pixels high
screen.setup(width=500, height=400)

# Ask for user's bet on which turtle that might win the race
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a rainbow color: ")

# Stores rainbow colors to be assigned to each turtle object
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Stores all turtle objects
all_turtles = []

# Initial Y-axis value
initial_y_axis = -90

# Position each turtle object at the starting position (X-axis: -230)
for turtle_index in range(0, 6):
    # Instantiate an object from Turtle class & use "turtle" cursor shape
    new_turtle = Turtle(shape="turtle")

    # Remove trace line
    new_turtle.penup()

    # Assign a corresponding color from the colors list to each turtle object
    new_turtle.color(colors[turtle_index])

    # Position each turtle on the same X-axis
    new_turtle.goto(x=-230, y=initial_y_axis)

    # Pad 40 paces between each turtle along the Y-axis
    initial_y_axis += 40

    # Store each turtle object on list
    all_turtles.append(new_turtle)

# Determines when to start the race
is_race_on = False

# Once a user placed a bet, the race starts
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Check if any of the turtles have reached the finish line (X-axis: 230)
        if turtle.xcor() > 230:
            is_race_on = False
            # Record the winning turtle
            winning_color = turtle.pencolor()

            # Check if the user's bet won
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Generates a random distance for each turtle to move forward
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
