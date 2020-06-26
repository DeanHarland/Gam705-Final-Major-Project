import pygame
import random
import math
import os
import sys
import wall
import character

# Open a window on screen
screenHeight = 900
screenWidth = 1000
screenWindow = pygame.display.set_mode([screenWidth, screenHeight])
screenWindow.fill((30, 90, 30))

# Title
pygame.display.set_caption("Cat And Mouse")

# Colour
black = (0,0,0)


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

wall1 = wall.Wall(0,0,screenWidth,10,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall(0,(screenHeight-10),screenWidth,10,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall(0,0,10,screenHeight,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall((screenWidth-10),0,10,screenHeight,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall(0,0,800,screenHeight,black,screenWindow)
WALLS.add(wall1)


def checkWallCollision(direction):
    # Check If colliding with wall for which ever direction is pressed.

    for wall in WALLS:

        if direction == pressed_left:
            if player.rect.colliderect(wall):
                player.canLeft = False
                print("cant move left")

            #if not player.rect.colliderect(wall):
               # player.canLeft = True

        if direction == pressed_right:
            if player.rect.colliderect(wall):
                player.canRight = False
                print("cant move right")

            #if not player.rect.colliderect(wall):
               # player.canRight = True






'''
def checkWallCollision(playerX, playerY, wallX, wallY):
    distance = math.sqrt((math.pow(wallX - playerX, 2)) + (math.pow(wallY - playerY, 2)))
    if distance < 28:
        return True
    else:
        return False
'''

# # # Main game loop # # #


player.walls = WALLS

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
            elif event.key == pygame.K_DOWN:
                pressed_down = True

        elif event.type == pygame.KEYUP:  # check for key releases
            if event.key == pygame.K_LEFT:
                pressed_left = False
                player.playerXSpeed = 0
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
                player.playerXSpeed = 0
            elif event.key == pygame.K_UP:
                pressed_up = False
            elif event.key == pygame.K_DOWN:
                pressed_down = False


    if pressed_left:


        checkWallCollision(pressed_left)

        if player.canLeft == True:
            playerX -= player.playerXSpeed

       # if player.canRight == False:
           # playerX -= player.playerXSpeed

        print("can right = " , player.canRight)
        print("can left = " , player.canLeft)



    if pressed_right:


        checkWallCollision(pressed_right)

        if player.canRight == True:
            playerX += player.playerXSpeed

        #if player.canLeft == False:
            #playerX += player.playerXSpeed

            #player.canLeft = True

        print("can right = ", player.canRight)
        print("can left = ", player.canLeft)



    if pressed_up:
        playerY -= player.playerYSpeed

    if pressed_down:
        playerY += player.playerYSpeed


    #player.canLeft = False
    #player.canRight = False

    player.drawPlayer(playerX,playerY)
    player.rect.x = playerX
    player.rect.y = playerY

    for wall in WALLS:
        wall.draw()

    pygame.display.update()
    clock.tick(60)