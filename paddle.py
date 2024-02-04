from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
    """Creates paddle object which can move up and down"""
    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_position)

    def up(self):
        """Moves paddle object 20 paces up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves paddle object 20 paces down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
