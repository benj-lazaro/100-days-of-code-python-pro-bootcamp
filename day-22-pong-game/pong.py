from turtle import Screen
from paddle import Paddle


# Create a screen with black background color & a dimension of 800x600
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# Turn off Turtle cursor animation
screen.tracer(0)

# Instantiate paddle objects & pass their starter screen coordinates
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Screen listen & bind keystrokes for paddle controls
screen.listen()

# Set right paddle controls
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Set left paddle controls
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    # Updates the screen; in conjunction with .tracer() method
    screen.update()

# Terminates the screen when clicked
screen.exitonclick()
