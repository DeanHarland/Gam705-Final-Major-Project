import pygame


playerSprite = pygame.image.load('monster.png')



class Player(pygame.sprite.Sprite):

    def __init__(self,width,height):

        super().__init__()

        self.image = pygame.image.load('monster.png')

        self.rect = self.image.get_rect()

    def drawPlayerTest(self,x,y,screen):

        self.screenWindow = screen
        screen.blit(self.image, (round(x), round(y)))
