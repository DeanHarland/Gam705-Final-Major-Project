import pygame
import random
import math
import os
import sys
import wall
import character

# Open a window on screen
screenHeight = 900
screenWidth = 1600
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

        self.playerXSpeed = 0.5
        self.playerYSpeed = 0.5
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



# Walls
WALLS = pygame.sprite.Group()

wall1 = wall.Wall(0,0,screenWidth,10,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall(0,(screenHeight-10),screenWidth,10,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall(0,0,10,screenHeight,black,screenWindow)
WALLS.add(wall1)
wall1 = wall.Wall((screenWidth-10),0,10,screenHeight,black,screenWindow)
WALLS.add(wall1)

def checkWallCollision(direction):
    for wall in WALLS:
        if direction == pressed_right:
            if player.rect.colliderect(wall):
               # player.playerXSpeed = 0
                player.canRight = False


        if direction == pressed_left:
            if player.rect.colliderect(wall):
              #  player.playerXSpeed = 0
                player.canLeft = False


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

        checkWallCollision(pressed_left)
        if player.canLeft == True:
            player.playerXSpeed = 0.5
            playerX -= player.playerXSpeed
            player.canRight = True

        elif player.canRight == False:
            player.playerXSpeed = 0.5
            playerX -= player.playerXSpeed
            player.canRight = True


    if pressed_right:
        checkWallCollision(pressed_right)
        if player.canRight == True:
            player.playerXSpeed = 0.5
            playerX += player.playerXSpeed
            player.canLeft = True

        elif player.canLeft == False:
            player.playerXSpeed = 0.5
            playerX += player.playerXSpeed
            player.canLeft = True

    if pressed_up:
        playerY -= player.playerYSpeed
    if pressed_down:
        playerY += player.playerYSpeed

    player.drawPlayer(playerX,playerY)
    player.rect.x = playerX
    player.rect.y = playerY

    for wall in WALLS:
        wall.draw()

    pygame.display.update()