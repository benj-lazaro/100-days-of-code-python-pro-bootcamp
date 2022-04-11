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
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
TOTAL_STATES = 50

while len(guessed_states) < TOTAL_STATES:
    # Receive answer from user & then convert it to titlecase
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    # Secret code to exit the game
    if answer_state == "Exit":
        # Create a .CSV file containing states that have not been guessed
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")
        break

    # Verify user's answer
    if answer_state in all_states:
        # Check is answer has not been guessed earlier
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            # Retrieve the state's X & Y coordinates
            state_data = data[data.state == answer_state]
            # Move the turtle cursor to the specified coordinates
            t.goto(int(state_data.x), int(state_data.y))
            # Write the guessed name of state
            t.write(answer_state)
            # t.write(state_data.state.item())
