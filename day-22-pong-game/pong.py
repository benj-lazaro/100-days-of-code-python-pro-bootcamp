from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


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

# Instantiate a ball object
ball = Ball()

# Instantiate a scoreboard object
scoreboard = Scoreboard()

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
    # Put the screen to sleep for 0.1 seconds to slow down the ball movement
    time.sleep(ball.move_speed)

    # Update the screen; in conjunction with .tracer() method
    screen.update()

    # Move the ball using its initial coordinates
    ball.move()

    # Detect ball collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce the ball
        ball.bounce_y()

    # Detect collision for both paddles & bounce the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle missed hitting the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# Detect when right paddle missed hitting the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


# Terminates the screen when clicked
screen.exitonclick()
