# ---------------------------------------------------------*\
# Title: Scoreboard
# Author: TM 2022
# ---------------------------------------------------------*/
#!/usr/bin/env python3

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ☠️", align=ALIGNMENT, font=("Courier", 40, "normal"))
        

# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\