import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Instantiate a turtle object
player = Player()

# Instantiate a car object
car_manager = CarManager()

# Bind keystroke for Turtle controller & listen
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate random cars & move them from the right to left side of the screen
    car_manager.create_car()
    car_manager.move_cars()
