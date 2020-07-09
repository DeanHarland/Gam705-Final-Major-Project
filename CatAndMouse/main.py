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
screenWindow.fill((20, 90, 20))

# Title
pygame.display.set_caption("Cat And Mouse")

# Colour
black = (0,0,0)
dimGrey = (50,50,50)
dimGrey1 = (128,128,128)
greyFloor = (96,96,96)
brown = (102,34,0)
browner = (77, 34, 0)
brownerer = (51, 17, 0)
darkestBrown = (26, 9, 0)
darkGreen = (0,51,0)
blue = (51,153,255)
darkBlue = (51,153,200)
treeGreen = (0,153,0)
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
spikePosSpeed = 5
spikeNegSpeed = -5
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
# Abilities
def shootSpike(x, y):
# Shoots a spike out infront of the players movement
    global spikeState
    spikeState = "fired"
    screenWindow.blit(spikeImg,(x,y))

# pounce

pounceLast = pygame.time.get_ticks()
pounceCooldown = 3000
pounceDistance = 100

def pounceAbility(x,y):
    print("pounce")
    leftPounce = x - pounceDistance
    rightPounce = x + pounceDistance
    upPounce = y - pounceDistance
    downPounce = y + pounceDistance

# Use current X + pounce distance to determine jump distance? but how to make it jump? speed up?
# Need sprint stamina for for loop?






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
pressed_Q = False
pressed_W = False

clock = pygame.time.Clock()


DECWALL  = pygame.sprite.Group()
wall99 = wall.Wall((screenWidth/4-5),(screenHeight-415),30,210,black,screenWindow)
wall98 = wall.Wall((screenWidth/4-5),115,30,310,black,screenWindow)
wall97 = wall.Wall((screenWidth/4-5),20,30,50,black,screenWindow)

wall96 = wall.Wall(10,(screenHeight/4-5),105,30,black,screenWindow)
wall95 = wall.Wall((screenWidth/4-115),(screenHeight/4-5),110,30,black   ,screenWindow)

wall94 = wall.Wall((screenWidth/4*3-5),115,30,310,black,screenWindow)
wall93 = wall.Wall((screenWidth/4*3-5),20,30,55,black,screenWindow)
# right side boot
wall92 = wall.Wall((screenWidth/4*3-5),495,30,310,black,screenWindow)

wall91 = wall.Wall((screenWidth/4*3+20),(screenHeight/3-5),100,30,black,screenWindow)
wall90 = wall.Wall((screenWidth-110),(screenHeight/3-5),100,30,black,screenWindow)
wall89 = wall.Wall((screenWidth/4*3+20),(screenHeight/4*3-5),100,30,black,screenWindow)
wall88 = wall.Wall((screenWidth-110),(screenHeight/4*3-5),100,30,black,screenWindow)

# MID SIDE?
wall87 = wall.Wall((screenWidth/4+55),screenHeight/4-5,(screenWidth/2-40),30,black,screenWindow)  # top mid
wall86 = wall.Wall((screenWidth/4 ),screenHeight/4*3-5,(screenWidth/2),30,black,screenWindow)  # bottom mid

# Fountain
wall85 = wall.Wall(screenWidth/2-80 ,screenHeight/2+45,160,30,black,screenWindow)
wall84 = wall.Wall(screenWidth/2-80 ,screenHeight/2-55,160,30,black,screenWindow)

wall83 = wall.Wall(screenWidth/2+40 ,screenHeight/2-50,30,120,black,screenWindow)
wall82 = wall.Wall(screenWidth/2-70,screenHeight/2-50,30,120,black,screenWindow)

wall81 = wall.Wall(screenWidth/2-50,screenHeight/2-50,100,100,blue,screenWindow)
# Bench
wall80 = wall.Wall(screenWidth/2+65 ,screenHeight/2-25,20,70,brown,screenWindow)
wall79 = wall.Wall(screenWidth/2-85 ,screenHeight/2-25,20,70,brown,screenWindow)

# Tree
wall78 = wall.Wall(1100 ,200,70,70,black,screenWindow)
wall77 = wall.Wall(1000 ,50,70,70,black,screenWindow)
wall76 = wall.Wall(950 ,190,50,50,black,screenWindow)

DECWALL.add(wall99,wall80,wall79,wall81,wall98,wall97, wall96,wall95,wall94,wall93,wall92,wall91,wall90,wall89,wall88,wall87,wall86,wall85,wall84,wall83,wall82, wall78,wall77, wall76)



# Walls - created a group and add each instance of wall to it.
WALLS = pygame.sprite.Group()
# X,Y,Height,Width,Height,Colour,Screen.

wall1 = wall.Wall(0,0,screenWidth,20,black,screenWindow)                    # top wall
wall2 = wall.Wall(0,(screenHeight-10),screenWidth,20,black,screenWindow)        # bot wall
wall3 = wall.Wall(0,0,10,screenHeight,black,screenWindow)                       # Left Wall
wall4 = wall.Wall((screenWidth-10),0,20,screenHeight,black,screenWindow)        # right wall
# LEFT SIDE
wall5 = wall.Wall((screenWidth/4),(screenHeight-410),20,200,dimGrey,screenWindow)
wall16 = wall.Wall((screenWidth/4),120,20,300,dimGrey,screenWindow)
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

# Fountain
wall27 = wall.Wall(screenWidth/2-75 ,screenHeight/2+50,150,20,dimGrey1,screenWindow)
wall28 = wall.Wall(screenWidth/2-75 ,screenHeight/2-50,150,20,dimGrey1,screenWindow)

wall29 = wall.Wall(screenWidth/2+45 ,screenHeight/2-50,20,100,dimGrey1,screenWindow)
wall30 = wall.Wall(screenWidth/2-65,screenHeight/2-50,20,100,dimGrey1,screenWindow)

#Tree
wall31 = wall.Wall(1105 ,205,60,60,treeGreen,screenWindow)
wall32 = wall.Wall(1005 ,55,60,60,treeGreen,screenWindow)

wall33 = wall.Wall(955 ,195,40,40,treeGreen,screenWindow)

WALLS.add(wall1,wall2,wall3,wall4,wall5,wall14,wall15,wall25,wall26,wall22,wall24,wall28,wall21,wall23,wall10,wall11, wall12, wall17,wall18,wall19,wall20,wall13,wall16, wall27,wall28,wall29,wall30,wall31,wall32, wall33)
player.walls = WALLS


# LEFT SIDE




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
    # Monster Spawn Floor
    pygame.draw.rect(screenWindow,darkGreen,[900,0,300,300])
    pygame.draw.rect(screenWindow, darkGreen, [1000, 200, 100, 280])

    # Middle Area
    pygame.draw.rect(screenWindow, greyFloor, [300, 580, 600, 100]) # B
    pygame.draw.rect(screenWindow, greyFloor, [300, 240, 600, 100]) # T
    pygame.draw.rect(screenWindow, greyFloor, [300, 240, 100, 400]) # L
    pygame.draw.rect(screenWindow, greyFloor, [800, 240, 100, 400]) # R


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
            elif event.key == pygame.K_q:
                pressed_Q = True
                if spikeState == "ready":
                    spikeX = playerX
                    spikeY = playerY
                    if pressed_left == True:
                        if pressed_up == True:
                            spikeYSpeed = (spikeNegSpeed+2)
                            spikeY -= 15
                            spikeXSpeed = (spikeNegSpeed+2)
                            spikeX -= 15
                        if pressed_down == True:
                            spikeXSpeed = (spikeNegSpeed+1)
                            spikeX -= 15
                            spikeYSpeed = (spikePosSpeed-1)
                            spikeY += 15
                        else:
                            spikeXSpeed = spikeNegSpeed
                            spikeX -= 15
                    elif pressed_right == True:
                        if pressed_up == True:
                            spikeYSpeed = (spikeNegSpeed+2)
                            spikeY -= 15
                            spikeXSpeed = (spikePosSpeed-2)
                            spikeX += 15
                        if pressed_down == True:
                            spikeXSpeed = (spikePosSpeed-1)
                            spikeX += 15
                            spikeYSpeed = (spikePosSpeed-1)
                            spikeY += 15
                        else:
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
            elif event.key == pygame.K_w:
                pressed_W = True
                now = pygame.time.get_ticks()
                if now - pounceLast >= pounceCooldown:
                    pounceLast = now
                    pounceAbility(playerX,playerY)


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
            elif event.key == pygame.K_q:
                pressed_Q = False
            elif event.key == pygame.K_w:
                pressed_W = False



    if pressed_left:
        playerX -= player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX += player.playerXSpeed

    if pressed_right:
        playerX += player.playerXSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerX -= player.playerXSpeed

    if pressed_up:
        playerY -= player.playerYSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerY += player.playerYSpeed

    if pressed_down:
        playerY += player.playerYSpeed
        player.rect.x = playerX
        player.rect.y = playerY
        checkForWalls()
        if player.isCollide == True:
            playerY -= player.playerYSpeed

    if pressed_W:
        pounceAbility(playerX,playerY)

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
    for wall in DECWALL:
        wall.draw()
    for wall in WALLS:
        wall.draw()

    pygame.display.update()
    clock.tick(60)