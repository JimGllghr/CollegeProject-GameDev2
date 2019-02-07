import pygame, math
import random

class Health(pygame.sprite.Sprite):
    def __init__(self, screen, scoreboard, player):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.crate = pygame.image.load("health.png")
        self.rect = self.crate.get_rect()
        self.image = self.crate
        self.rect.center = (2000, 2000)
        
        self.healthRespawn = 1
        self.score = scoreboard
        self.playerTank = player
        
        self.playerSprite = pygame.sprite.GroupSingle(sprite=self.playerTank)
        
    def update(self):
        collectPackage = pygame.sprite.spritecollide(self, self.playerSprite, False)
        if collectPackage:
            self.score.health=100
            self.rect.x = 2000
            self.rect.y = 2000
            self.healthRespawn=1
            
        if self.healthRespawn>1800:
            self.reset()
            self.healthRespawn=1
        self.healthRespawn+=1

    def reset(self):
        randomY = random.randint(1,640)
        randomX = random.randint(1,920)
        self.rect.center = (randomX, randomY)
        self.x = randomX
        self.y = randomY

    def used(self):
        self.x = 2000
        self.y = 2000
        self.rect.center = (self.x, self.y)