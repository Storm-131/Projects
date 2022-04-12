# ---------------------------------------------------------*\
# Title: Paddle
# Author: TM 2022
# ---------------------------------------------------------*/
#!/usr/bin/env python3

from turtle import Turtle

STEPSIZE = 25

class Paddle (Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.width = 20
        self.height = 20
        self.x_pos = x
        self.y_pos = y
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(self.x_pos, self.y_pos)

    def up(self):
        if self.y_pos <= 220:
          self.y_pos += STEPSIZE
          self.goto(self.x_pos, self.y_pos)   

    def down(self):
        if self.y_pos >= -220:
          self.y_pos -= STEPSIZE
          self.goto(self.x_pos, self.y_pos)

# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\
