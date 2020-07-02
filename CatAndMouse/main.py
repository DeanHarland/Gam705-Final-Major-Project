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

# Player
playerX = screenWidth - 100
playerY = 100


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

clock = pygame.time.Clock()

# Walls - created a group and add each instance of wall to it.
WALLS = pygame.sprite.Group()
# X,Y,Height,Width,Height,Colour,Screen.

wall1 = wall.Wall(0,0,screenWidth,20,black,screenWindow)                    #top wall
WALLS.add(wall1)
wall2 = wall.Wall(0,(screenHeight-10),screenWidth,20,black,screenWindow)        #bot wall
WALLS.add(wall2)
wall3 = wall.Wall(0,0,10,screenHeight,black,screenWindow)                       # Left Wall
WALLS.add(wall3)
wall4 = wall.Wall((screenWidth-10),0,20,screenHeight,black,screenWindow)        #right wall
WALLS.add(wall4)
                                                                                # Try adding all at the same time
# LEFT SIDE
wall5 = wall.Wall((screenWidth/4),(screenHeight-410),20,400,dimGrey,screenWindow)
WALLS.add(wall5)



# RIGHT SIDE
wall10 = wall.Wall((screenWidth/4*3),20,20,400,dimGrey,screenWindow)
WALLS.add(wall10)


# MID SIDE?
wall10 = wall.Wall((screenWidth/4),screenHeight/4,(screenWidth/2),20,dimGrey,screenWindow)  #top mid
WALLS.add(wall10)

wall11 = wall.Wall((screenWidth/4 ),screenHeight/4*3,(screenWidth/2),20,dimGrey,screenWindow)  #bottom mid
WALLS.add(wall11)

'''
def checkWallCollision(direction):
    # Check If colliding with wall for which ever direction is pressed.

    for wall in WALLS:

        if direction == pressed_left:
            if player.rect.colliderect(wall):
                player.canLeft = False
                print("cant move left")


        elif direction == pressed_right:
            if player.rect.colliderect(wall):
                player.canRight = False
                print("cant move right")

'''


def checkForWalls():

    for wall in WALLS:

        if player.rect.colliderect(wall):
            player.isCollide = True
            break
        if not player.rect.colliderect(wall):
            player.isCollide = False


player.walls = WALLS

'''
def checkWallCollision(playerX, playerY, wallX, wallY):
    distance = math.sqrt((math.pow(wallX - playerX, 2)) + (math.pow(wallY - playerY, 2)))
    if distance < 28:
        return True
    else:
        return False
'''

# # # Main game loop # # #




running = True
while running:

    screenWindow.fill((30, 90, 30))


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


    if pressed_left:

        playerX -= player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX += player.playerXSpeed
            #checkForWalls()
        print(player.isCollide)


    if pressed_right:

        playerX += player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX -= player.playerXSpeed
            #checkForWalls()
        print(player.isCollide)

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


    player.drawPlayer(playerX,playerY)
    player.rect.x = playerX
    player.rect.y = playerY

    for wall in WALLS:
        wall.draw()

    pygame.display.update()
    clock.tick(60)