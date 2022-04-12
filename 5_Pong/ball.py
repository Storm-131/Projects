# ---------------------------------------------------------*\
# Title: Ball
# Author: TM 2022
# ---------------------------------------------------------*/
#!/usr/bin/env python3

from turtle import Turtle

STARTSPEED = 1

class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = 10  # For collision with top / bottom
        self.y_move = 10
        self.speed = STARTSPEED
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(self.x_pos, self.y_pos)

    def move(self):
        self.x_pos += self.x_move * self.speed
        self.y_pos += self.y_move * self.speed
        self.setpos(self.x_pos, self.y_pos)

    def bounce_y (self):
        self.y_move *= -1
        
    def bounce_x (self):
        self.x_move *= -1
        
    def reset (self):
        self.x_pos = 0
        self.y_pos = 0
        self.speed = STARTSPEED
        self.bounce_x()
        self.bounce_y()
        
    def increase_speed(self):
      self.speed += 0.05
      
# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\
