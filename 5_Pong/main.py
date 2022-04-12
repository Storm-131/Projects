# ---------------------------------------------------------*\
# Title: Pong-Game (Main)
# Author: TM 2022
# ---------------------------------------------------------*/
#!/usr/bin/env python3

import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen-Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)    # Turn animations of turtle off

# Screen-Separator
separator = Turtle()
separator.penup()
separator.goto(0, -300)
separator.color("white")
separator.pendown()
separator.setheading(90)
for _ in range(30):
    separator.forward(10)
    separator.penup()
    separator.forward(10)
    separator.pendown() 
separator.hideturtle()

# Major-Objects
ball = Ball()
paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
scoreboard_l = Scoreboard(-200)
scoreboard_r = Scoreboard(200)

# Keystroke - Events
screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.update()

# Game Loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
 
     # Detect collision with wall
    if ball.y_pos >= 280 or ball.y_pos <= -280:
        ball.bounce_y()
 
    # Detect collision with r_paddle    
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.increase_speed()
        ball.bounce_x()
        
    # Detect collision with r_paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.increase_speed()
        ball.bounce_x()
        
    # Detect missing paddle (ball out) - Right side loses
    if ball.x_pos > 380 :
        scoreboard_l.increase_score()
        ball.reset()    
    
    # Detect missing paddle (ball out) - Left side loses
    if ball.x_pos > 380 or ball.x_pos < -380:
        scoreboard_r.increase_score()
        ball.reset()

screen.exitonclick()

# -------------------------Notes-----------------------------------------------*\
# 100 Days of Code: The complete Python Pro Bootcamp for 2022 (App Brewery)
# -----------------------------------------------------------------------------*\
