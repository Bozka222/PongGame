from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard, DashedLine
import time

RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong game 🔴")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
score_board = Scoreboard()
line = DashedLine()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_continues = True
while game_continues:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #  Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Needs to bounce

    #  Detect collision with the paddles
    if ball.xcor() > 335 and ball.distance(right_paddle) < 50 and ball.x_move > 0 \
            or ball.xcor() < -335 and ball.distance(left_paddle) < 50 and ball.x_move < 0:
        ball.bounce_x()

    #  Detect right miss
    if ball.xcor() > 400:
        ball.reset_position()
        score_board.left_point()
        time.sleep(1)

    #  Detect left miss
    if ball.xcor() < -400:
        ball.reset_position()
        score_board.right_point()
        time.sleep(1)

    #  End game if one player has 10 points
    if score_board.left_score == 10 or score_board.right_score == 10:
        game_continues = False

screen.exitonclick()
