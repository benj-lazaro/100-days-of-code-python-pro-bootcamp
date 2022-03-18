from turtle import Turtle, Screen


def move_forwards():
    """Moves the turtle cursor forward by 10 paces"""
    tim.forward(10)


def move_backwards():
    """Move the turtle cursor backwards by 10 paces"""
    tim.backward(10)


def move_leftwards():
    """Rotates the turtle cursor counter-clockwise or leftwards by 10 paces"""
    tim.left(10)


def move_rightwards():
    """Rotates the turtle cursor clockwise or rightwards by 10 pacws"""
    tim.right(10)


def clear_screen():
    """Clears the turtle screen and repositions the turtle cursor to its initial state"""
    tim.clear()
    tim.reset()


# Instantiate objects from their respective classes
tim = Turtle()
tim.speed("fastest")
screen = Screen()

# Set up an event listener; bind keys with corresponding high-order functions
screen.listen()
# NOTE: Use keyword args instead of position args
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_leftwards, key="a")
screen.onkey(fun=move_rightwards, key="d")

screen.exitonclick()
