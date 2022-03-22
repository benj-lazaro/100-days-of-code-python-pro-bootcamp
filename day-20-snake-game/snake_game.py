from turtle import Screen, Turtle
from snake import Snake
import time

# Instantiate object from class Screen
screen = Screen()

# Setup screen as 600 pixels wide by 600 pixels high, black background color & title of "My Snake Game"
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Call and turn off the tracer() method of the Screen class
screen.tracer(0)

# Instantiate an object from Snake class
snake = Snake()

game_is_on = True

while game_is_on:
    # Updates the screen to display; moving  the 3-segment starter snake body as a single piece
    screen.update()
    # Update the screen every 0.1 seconds
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
