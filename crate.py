import pygame, math
import random

class Crate(pygame.sprite.Sprite):
    def __init__(self, screen, (x, y), playerTank, scoreboard):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.crate = pygame.image.load("crate.jpg")
        self.rect = self.crate.get_rect()
        self.image = self.crate
        self.rect.center = (x, y)
        self.x = x
        self.y = y
    
        self.player = playerTank
        self.score = scoreboard
        
        self.playerSprite = pygame.sprite.GroupSingle(sprite=self.player)

    def reset(self):
        randomY = random.randint(1,640)
        randomX = random.randint(1,920)
        self.rect.center = (randomX, randomY)
        self.x = randomX
        self.y = randomY
        
    def update(self):
        self.checkCollision()
    
    def checkCollision(self):
        collectPackage = pygame.sprite.spritecollide(self, self.playerSprite, False)
        if collectPackage:
            self.score.score+=1
            self.reset()
        