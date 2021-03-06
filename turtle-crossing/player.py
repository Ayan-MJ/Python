from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto_starting_line()
        self.setheading(90)  # facing the direction

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def goto_starting_line(self):
        self.goto(STARTING_POSITION)

    def crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

