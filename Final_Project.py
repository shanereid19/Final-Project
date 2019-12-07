import pygame
import turtle

"""
https://www.youtube.com/watch?v=C6jJg9Zan7w&t=232s
I watched this video for guidenace and help.
"""

# For my project I plan to create a game simialr to pong but modified to be more like a soccer game.
# The game is called "Soccer Pong".
# Therefore, as a reulst I have imported "pygame", "turtle" and "time" to use in the interface of the game.
# I will use pygame to design the game, turtle to design the characters and time is an important variable in games and soccer alike.

pygame.init()
# This was done to iniatlise the game.

#This is done to set up the game window for the program.
wn = turtle.Screen()
wn.title("Soccer Pong")
wn.bgcolor("dark green")
wn.setup(width=800, height=600)
wn.tracer(0)


# This is a counter to keep track of the score for both players.
score_a = 0
score_b = 0

# This is Paddle A
"Turn this into a function."
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# This is Paddle B
"Turn this into a function."
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# This is the ball that will be used in the game.
"Turn this into a function."
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# This is the turtle commands that draws the set up of the game.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# The below functions are used to move the paddles up and down for the game.
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
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

# These are the keyboard controls for the game.
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#def main():
    # This is the main game loop of the program.

while True:
    wn.update()	

	# This moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    # These if staements are done to make sure that players get points for hitting the ball 
    # against the border of the window.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # These if statements are used in the gameplay to make the game continue as the Paddle and ball collide.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
