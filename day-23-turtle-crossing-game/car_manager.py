from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a car with random color & starting position on the Y-axis of the screen"""
        # Generate a car ONLY when the random number is == 1
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves a car from the right to the left side of the screen"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increases the speed of the car after the player levels up"""
        self.car_speed += MOVE_INCREMENT
