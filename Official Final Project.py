import turtle

#These are my Acknowledgments/Citations:
"""
https://www.youtube.com/watch?v=C6jJg9Zan7w&t=232s
I watched this video for guidenace and help.
"""

#These are certain variabes that need to be defined outside of functions as they will be used within various functions.
#They will have a global definitions.
pen = turtle.Turtle()
pen.hideturtle()

#These are customiasble variables for the players.
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()

def screen_set_up():
    #This function sets up the window for the game to be played and the screen.
    global pen
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.bgcolor("dark green")
    window.title("Soccer Pong")

def start_screen():
    #This function is the start screen of the game.
    #This will be the first thing the user sees when they run the program.
    global pen
    pen.pencolor("white")
    pen.hideturtle()
    pen.write("Welcome to Soccer Pong!!!\n Press ENTER to start", align = "center", font = ("Ariel", 40, "normal"))
    window = turtle.Screen()
    window.listen()
    window.onkeypress(instructions, "Return")

def instructions():
    #This is the screen that tells the users their instructions for the game.
    #The "how to play" screen.
    #This will be the screen that comes up secnd to the start screen for the first player.
    global pen
    pen.clear()
    pen.hideturtle()
    pen.pencolor("white")
    pen.hideturtle()
    pen.write("How To Play\nPlayer 1:\nW: moves the paddle up\nand S: moves the paddle down\nPlayer 2:\nThe up arrow moves the paddle up\nand the down arrow moves the paddle down\n\nPress ENTER to continue.", align = "center", font = ("Ariel", 20, "normal"))
    window = turtle.Screen()
    window.listen()
    window.onkeypress(first_player, "Return")

def first_player():
    #This will be the screen that comes up third to the start screen for the first player.
    #Within this screen, the first user will be able to select options for playing the game.
    global pen
    global paddle_a
    pen.setposition(0, -200)
    pen.clear()
    pen.hideturtle()
    pen.pencolor("white")
    pen.write("Player 1:\nChoose a number 1-4\n for the color of the paddle\n1. White\n2. Black\n3. Blue\n4. Red\n Press ENTER when ready,\n to start game." , align = "center", font = ("Ariel", 30, "normal"))
    window = turtle.Screen()
    window.listen()
    window.onkeypress(paddle_a_color_white, "1")
    window.onkeypress(paddle_a_color_black, "2")
    window.onkeypress(paddle_a_color_blue, "3")
    window.onkeypress(paddle_a_color_red, "4")
    window.onkeypress(second_player, "Return")

#These four functions houses the options for Player A to choose from for the paddle color.
def paddle_a_color_white():
    global paddle_a
    paddle_a.color("white")

def paddle_a_color_black():
    global paddle_a
    paddle_a.color("black")

def paddle_a_color_blue():
    global paddle_a
    paddle_a.color("blue")

def paddle_a_color_red():
    global paddle_a
    paddle_a.color("red")

def second_player():
    #This will be the screen that comes up fourth to the start screen for the second player.
    #Within this screen, the second user will be able to select options for playing the game.
    global pen
    global paddle_b
    pen.setposition(0, -200)
    pen.clear()
    pen.hideturtle()
    pen.pencolor("white")
    pen.write("Player 2:\nChoose a number 1-4\n for the color of the paddle\n1. White\n2. Black\n3. Blue\n4. Red\n Press ENTER when ready,\n to start game." , align = "center", font = ("Ariel", 30, "normal"))
    window = turtle.Screen()
    window.listen()
    window.onkeypress(paddle_b_color_white, "1")
    window.onkeypress(paddle_b_color_black, "2")
    window.onkeypress(paddle_b_color_blue, "3")
    window.onkeypress(paddle_b_color_red, "4")
    window.onkeypress(game_ball, "Return")

#These four functions houses the options for Player B to choose from for the paddle color.
def paddle_b_color_white():
    global paddle_b
    paddle_b.color("white")

def paddle_b_color_black():
    global paddle_b
    paddle_b.color("black")

def paddle_b_color_blue():
    global paddle_b
    paddle_b.color("blue")

def paddle_b_color_red():
    global paddle_b
    paddle_b.color("red")

def game_ball():
    #This will be the screen that comes up fifth to the start screen for both players.
    #Within this screen, both user will be able to select options for playing the game.
    #This should be a consensus between the two players.
    global pen
    global ball
    pen.setposition(0, -200)
    pen.clear()
    pen.hideturtle()
    pen.pencolor("white")
    pen.write("Both Players:\nChoose a number 1-4\n for the color of the ball\n1. White\n2. Black\n3. Blue\n4. Red\n Press ENTER when ready,\n to start game." , align = "center", font = ("Ariel", 30, "normal"))
    window = turtle.Screen()
    window.listen()
    window.onkeypress(ball_color_white, "1")
    window.onkeypress(ball_color_black, "2")
    window.onkeypress(ball_color_blue, "3")
    window.onkeypress(ball_color_red, "4")
    window.onkeypress(game, "Return")

#These four functions houses the options for both players to choose from for the color of the ball.
def ball_color_white():
    global ball
    ball.color("white")

def ball_color_black():
    global ball
    ball.color("black")

def ball_color_blue():
    global ball
    ball.color("blue")

def ball_color_red():
    global ball
    ball.color("red")

def game():
    # This is the turtle commands that draws the set up of the game.
    
    global pen
    pen.clear()
    pen.hideturtle()

    # This is Paddle A
    global paddle_a
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # This is Paddle B
    global paddle_b
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # This is the ball that will be used in the game.
    global ball
    ball.speed(0)
    ball.shape("square")
    #ball.color("white")
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

    # This is a counter to keep track of the score for both players.
    score_a = 0
    score_b = 0

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
    wn = turtle.Screen()
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

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

def main():
    #This is the main function.
    #This houses all the other functions and calls them so as to get the program running.
    screen_set_up()
    start_screen()
    
    #Start main game interactivity loop.
    turtle.mainloop()

#Calling the main function.
main()