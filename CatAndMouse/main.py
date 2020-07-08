import pygame
import random
import math
import os
import sys
import wall
import character

# Open a window on screen
screenHeight = 900
screenWidth = 1200
screenWindow = pygame.display.set_mode([screenWidth, screenHeight])
screenWindow.fill((30, 90, 30))

# Title
pygame.display.set_caption("Cat And Mouse")

# Colour
black = (0,0,0)
dimGrey = (105,105,105)
brown = (102,34,0)
browner = (77, 34, 0)
brownerer = (51, 17, 0)
darkestBrown = (26, 9, 0)

# Player
playerX = screenWidth - 100
playerY = 100

# Spike ability
spikeImg = pygame.image.load("nail.png")
spikeX = 0
spikeY = playerY
spikeXSpeed = 0
spikeYSpeed = 0
spikeState = "ready"
spikePosSpeed = 4
spikeNegSpeed = -4
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()

        self.playerXSpeed = 0
        self.playerYSpeed = 0
        self.walls = None

        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.isCollide = False

        #removable?
        self.canLeft = True
        self.canRight = True


    def drawPlayer(self,x,y):
        screenWindow.blit(self.image, (round(x), round(y)))

def shootSpike(x, y):

    global spikeState
    spikeState = "fired"
    screenWindow.blit(spikeImg,(x,y))


# def spikeCollision():
    # for wall in WALLS:
        # if spike


player = Player(30,30)
player.rect.x = playerX
player.rect.y = playerY


pygame.init()
# Game over/restart
gameOVer = False

# Keyboard Variables
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = False
pressed_space = False

clock = pygame.time.Clock()

# Walls - created a group and add each instance of wall to it.
WALLS = pygame.sprite.Group()
# X,Y,Height,Width,Height,Colour,Screen.

wall1 = wall.Wall(0,0,screenWidth,20,black,screenWindow)                    # top wall

wall2 = wall.Wall(0,(screenHeight-10),screenWidth,20,black,screenWindow)        # bot wall
wall3 = wall.Wall(0,0,10,screenHeight,black,screenWindow)                       # Left Wall
wall4 = wall.Wall((screenWidth-10),0,20,screenHeight,black,screenWindow)        # right wall
# LEFT SIDE
wall5 = wall.Wall((screenWidth/4),(screenHeight-410),20,200,dimGrey,screenWindow)
wall14 = wall.Wall((screenWidth/4),120,20,300,dimGrey,screenWindow)
wall15 = wall.Wall((screenWidth/4),20,20,50,dimGrey,screenWindow)
# house home
wall25 = wall.Wall((screenWidth/4),screenHeight/4*3,25,100,brown,screenWindow)
wall26 = wall.Wall((screenWidth/4),screenHeight-70,25,60,brown,screenWindow)
wall22 = wall.Wall(10,(screenHeight/4*3),100,25,brown,screenWindow)
wall24 = wall.Wall((screenWidth/4-110),(screenHeight/4*3),110,25,brown,screenWindow)
wall28 = wall.Wall((screenWidth/4-100),(screenHeight/4*3+90),25,80,brown,screenWindow)
# left left side
wall21 = wall.Wall(10,(screenHeight/4),100,20,dimGrey,screenWindow)
wall23 = wall.Wall((screenWidth/4-110),(screenHeight/4),110,20,dimGrey,screenWindow)
# RIGHT SIDE TOP
wall10 = wall.Wall((screenWidth/4*3),120,20,300,dimGrey,screenWindow)
wall11 = wall.Wall((screenWidth/4*3),20,20,50,dimGrey,screenWindow)
# right side boot
wall12 = wall.Wall((screenWidth/4*3),500,20,300,dimGrey,screenWindow)
# right right side
wall17 = wall.Wall((screenWidth/4*3+20),(screenHeight/3),100,20,dimGrey,screenWindow)
wall18 = wall.Wall((screenWidth-110),(screenHeight/3),100,20,dimGrey,screenWindow)
wall19 = wall.Wall((screenWidth/4*3+20),(screenHeight/4*3),100,20,dimGrey,screenWindow)
wall20 = wall.Wall((screenWidth-110),(screenHeight/4*3),100,20,dimGrey,screenWindow)
# MID SIDE?
wall13 = wall.Wall((screenWidth/4+60),screenHeight/4,(screenWidth/2-40),20,dimGrey,screenWindow)  # top mid
wall14 = wall.Wall((screenWidth/4 ),screenHeight/4*3,(screenWidth/2),20,dimGrey,screenWindow)  # bottom mid
WALLS.add(wall1,wall2,wall3,wall4,wall5,wall14,wall15,wall25,wall26,wall22,wall24,wall28,wall21,wall23,wall10,wall11, wall12, wall17,wall18,wall19,wall20,wall13,wall14)
player.walls = WALLS

def drawFloors():
    # pygame.draw.rect(screenWindow,dimGrey,[10,680,300,420])
    pygame.draw.rect(screenWindow, browner, [10, 680, 30, 300])
    pygame.draw.rect(screenWindow, brownerer, [40, 680, 30, 300])
    pygame.draw.rect(screenWindow, browner, [70, 680, 30, 300])
    pygame.draw.rect(screenWindow, brownerer, [100, 680, 30, 300])
    pygame.draw.rect(screenWindow, browner, [130, 680, 30, 300])
    pygame.draw.rect(screenWindow, brownerer, [160, 680, 30, 300])
    pygame.draw.rect(screenWindow, browner, [190, 680, 30, 300])
    pygame.draw.rect(screenWindow, brownerer, [220, 680, 30, 300])
    pygame.draw.rect(screenWindow, browner, [250, 680, 30, 300])
    pygame.draw.rect(screenWindow, brownerer, [280, 680, 30, 300])

def checkForWalls():

    for wall in WALLS:

        if player.rect.colliderect(wall):
            player.isCollide = True
            break
        if not player.rect.colliderect(wall):
            player.isCollide = False



# # # Main game loop # # #

running = True
while running:

    screenWindow.fill((30, 90, 30))
    drawFloors()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:
                pressed_left = True
                player.playerXSpeed = 3
            elif event.key == pygame.K_RIGHT:
                pressed_right = True
                player.playerXSpeed = 3
            elif event.key == pygame.K_UP:
                pressed_up = True
                player.playerYSpeed = 3
            elif event.key == pygame.K_DOWN:
                pressed_down = True
                player.playerYSpeed = 3
            elif event.key == pygame.K_SPACE:
                pressed_space = True
                if spikeState == "ready":
                    spikeX = playerX
                    spikeY = playerY
                    if pressed_left == True:
                        spikeXSpeed = spikeNegSpeed
                        spikeX -= 15
                    elif pressed_right == True:
                        spikeXSpeed = spikePosSpeed
                        spikeX += 15
                    elif pressed_up == True:
                        spikeYSpeed = spikeNegSpeed
                        spikeY -= 15
                    elif pressed_down == True:
                        spikeYSpeed = spikePosSpeed
                        spikeY += 15
                    else:
                        spikeYSpeed = 4
                    shootSpike(spikeX, spikeY)


        elif event.type == pygame.KEYUP:  # check for key releases
            if event.key == pygame.K_LEFT:
                pressed_left = False
                player.playerXSpeed = 3
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
                player.playerXSpeed = 3
            elif event.key == pygame.K_UP:
                pressed_up = False
                player.playerYSpeed = 3
            elif event.key == pygame.K_DOWN:
                pressed_down = False
                player.playerYSpeed = 3
            elif event.key == pygame.K_SPACE:
                pressed_space = False


    if pressed_left:

        playerX -= player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX += player.playerXSpeed
            #checkForWalls()



    if pressed_right:

        playerX += player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX -= player.playerXSpeed
            #checkForWalls()


    if pressed_up:
        playerY -= player.playerYSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerY += player.playerYSpeed
            #checkForWalls()

    if pressed_down:
        playerY += player.playerYSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerY -= player.playerYSpeed
            #checkForWalls()

    #if pressed_space:
        #spikeState = True
        #shootSpike(playerX, playerY)

       # spikeY -= spikeYSpeed
    spikeCollide = False
    if spikeState == "fired":
        shootSpike(spikeX, spikeY)
        spikeX += spikeXSpeed
        spikeY += spikeYSpeed
        spikeRect = pygame.Rect(spikeX, spikeY,30,30)
        for wall in WALLS:

            if spikeRect.colliderect(wall):
                spikeCollide = True
                spikeXSpeed = 0
                spikeYSpeed = 0
                spikeState = "ready"
                break
            if not spikeRect.colliderect(wall):
                spikeCollide = False






    player.drawPlayer(playerX,playerY)
    player.rect.x = playerX
    player.rect.y = playerY

    for wall in WALLS:
        wall.draw()

    pygame.display.update()
    clock.tick(60)