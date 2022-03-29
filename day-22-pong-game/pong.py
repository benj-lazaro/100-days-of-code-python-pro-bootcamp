from turtle import Screen, Turtle


def up():
    """Moves the paddle up by 20 paces"""
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    paddle.speed("fastest")


def down():
    """Moves the paddle down by 20 paces"""
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    paddle.speed("fastest")


# Create a screen with black background color & a dimension of 800x600
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Set up the right-side white colored paddle (20x100) located at position 250 x 0
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setposition(x=350, y=0)

# Screen listen to keystrokes for paddle controls
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

# Terminates the screen when clicked
screen.exitonclick()
