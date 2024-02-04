from turtle import Turtle


class Ball(Turtle):
    """Creates ball object which moves diagonally"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        """Moves ball object by 10 paces in x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Changes ball move direction in y-axes (collision with wall)"""
        self.y_move *= -1

    def bounce_x(self):
        """Changes ball move direction in x-axes (collision with paddles). Also adds movement speed"""
        self.x_move *= -1
        self.move_speed *= 0.9
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets ball position to 0,0"""
        self.bounce_x()
        self.move_speed = 0.05
        self.goto(x=0, y=0)
