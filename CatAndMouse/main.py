import pygame
import random
import math
import os
import sys
import wall


# Colour
black = (0,0,0)

# Player
playerSprite = pygame.image.load('monster.png')
playerX = 1500
playerY = 100
playerXSpeed = 0.5
playerYSpeed = 0.5

def drawPlayer(x,y):
    screenWindow.blit(playerSprite, (round(x),round(y)))

# Open a window on screen
screenHeight = 900
screenWidth = 1600
screenWindow = pygame.display.set_mode([screenWidth, screenHeight])
screenWindow.fill((30, 90, 30))

# Title
pygame.display.set_caption("Cat And Mouse")

# Game over/restart
gameOVer = False

# Keyboard Variables
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False


# Walls
WALLS = pygame.sprite.Group()

wall1 = wall.Wall(0,0,screenWidth,10,black,screenWindow)
wall2 = wall.Wall(0,(screenHeight-10),screenWidth,10,black,screenWindow)
wall3 = wall.Wall(0,0,10,screenHeight,black,screenWindow)
wall4 = wall.Wall((screenWidth-10),0,10,screenHeight,black,screenWindow)

WALLS.add(wall1,wall2,wall3,wall4)



# # # Main game loop # # #
pygame.init()



running = True
while running:

    screenWindow.fill((30, 90, 30))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
            elif event.key == pygame.K_UP:
                pressed_up = True
            elif event.key == pygame.K_DOWN:
                pressed_down = True

        elif event.type == pygame.KEYUP:  # check for key releases
            if event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
            elif event.key == pygame.K_UP:
                pressed_up = False
            elif event.key == pygame.K_DOWN:
                pressed_down = False

    if pressed_left:
        playerX -= playerXSpeed
    if pressed_right:
        playerX += playerXSpeed
    if pressed_up:
        playerY -= playerYSpeed
    if pressed_down:
        playerY += playerYSpeed





    drawPlayer(playerX,playerY)

    for wall in WALLS:
        wall.draw()

    pygame.display.update()