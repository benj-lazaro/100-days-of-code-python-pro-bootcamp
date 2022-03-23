from turtle import Screen
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

# Listen for keystrokes (snake controls)
screen.listen()
# Bind keystrokes to the corresponding Snake class methods
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Refresh the screen to display; moving  the 3-segment starter snake body as a single piece
    screen.update()
    # Delay screen update for 0.1 seconds
    time.sleep(0.1)
    # Call the .move() method of the Snake class and then move the snake segment
    snake.move()

screen.exitonclick()
