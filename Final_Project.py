import pygame

pygame.init()

"""
Watched tutorials of functions and how to make screens from the pygame website
https://pythonprogramming.net/pygame-python-3-part-1-intro/

"""

gameDISPLAY = pygame.display.set_mode((800,600))

pygame.display.set_caption("Soccer Pong")

clock = pygame.time.Clock()

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
    
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDISPLAY.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",100)
        TextSurf, TextRect = text_object("Soccer Pong", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(30)

game_intro()