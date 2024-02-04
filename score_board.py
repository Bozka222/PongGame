from turtle import Turtle


class Scoreboard(Turtle):
    """Creates scoreboard numbers"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates scoreboard numbers"""
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        """Adds one point to left player"""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Adds one point to right player"""
        self.right_score += 1
        self.update_scoreboard()


class DashedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.sety(300)
        for _ in range(30):
            self.pendown()
            self.sety(self.ycor() - 10)
            self.penup()
            self.sety(self.ycor() - 10)
