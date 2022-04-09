# Pong Game

import turtle
import os

from numpy import square

wn = turtle.Screen()
wn.title("Pong game by @dvip")
wn.bgcolor("black")
wn.tracer(0)
wn.setup(width=1000, height=1000)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("lightgreen")
paddle_a.penup()
paddle_a.goto(-470, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lightgreen")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(460, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = -6

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
    
# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
    
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Check
    if ball.ycor() > 420:
        ball.sety(420)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
        
    if ball.ycor() < -420:
        ball.sety(-420)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
        
    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        # ball.dx *= 1.05
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = 'center', font = ('Courier', 28, 'normal'))
        os.system("afplay bounce.wav&")
        
    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        # ball.dy *= 1.05
        score_b += 1
        pen.clear()
        os.system("afplay bounce.wav&")
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = 'center', font = ('Courier', 28, 'normal'))
        
    # Paddle and ball collision
    
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1
        
    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.sety(-440)
        ball.dx *= -1