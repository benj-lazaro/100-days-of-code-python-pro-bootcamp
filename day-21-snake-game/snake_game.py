from turtle import Screen
from snake import Snake
from food import Food
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

# Instantiate an object from Food class
food = Food()

# Listen for keystrokes (snake controls)
screen.listen()
# Bind keystrokes to the corresponding Snake class methods
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Refresh the screen to display; moves the 3-segment starter snake body as a single entity
    screen.update()
    # Delay screen update for 0.1 second
    time.sleep(0.1)
    # Call the .move() method of the Snake class to move the snake around the screen
    snake.move()

    # Detect collision of snake with food
    # Check distance between snake head and within 15 pixels of the food coordinates
    if snake.head.distance(food) < 15:
        # Move food to a new location within teh screen
        food.refresh()


screen.exitonclick()
