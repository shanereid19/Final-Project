import pygame
import time

# For my project I plan to create a game simialr to pong but modified to be more like a soccer game.
# The game is called "Soccer Pong".
# Therefore, as a reulst I have imported "pygame" and "time" to use in the interface of the game.
# I will use pygame to design the game and time is an important variable in games and soccer alike.

pygame.init()
# This was done to iniatlise the game.

"""
Watched tutorials of functions and how to make screens from the pygame website
https://pythonprogramming.net/pygame-python-3-part-1-intro/
"""

display_width = 800
#This is the display width of the window that the game will be played in.
display_height = 600
##This is the display height of the window that the game will be played in.

black = (0,0,0)
white = (255,255,255)
#These are the colors that the game will use.

gameDISPLAY = pygame.display.set_mode((display_width, display_height))
# This is the display window in which the game will be played.

pygame.display.set_caption("Soccer Pong")
# This is the title of the display window.

clock = pygame.time.Clock()
# This will be the clock that helps to set the game time for each match.

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()

def game_intro():
    #This will be the introductary screen to the game.
    
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDISPLAY.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",100)
        TextSurf, TextRect = text_objects("Soccer Pong", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(30)

def game_loop():
    
    #This function is the function that allows theuser to exit the game.
    #When the user hits the "x" to close the window, the window will be closed.

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()