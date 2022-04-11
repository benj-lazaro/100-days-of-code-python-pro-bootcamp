import turtle
import pandas

# Create an instance of the Screen class
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the .GIF file as a background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reads the CSV data file
us_states_data = pandas.read_csv("50_states.csv")

# Gets input from the player / user
answer_state = turtle.textinput(title="Guess the State", prompt="What's another state name?")
print(answer_state)
