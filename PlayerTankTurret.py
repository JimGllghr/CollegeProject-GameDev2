import pygame, math

from FShell import fShell

class playerTurret(pygame.sprite.Sprite):
    def __init__(self, screen, playerTank, allsprites, prey):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.turret = pygame.image.load("tankturret.png")
        self.turret = self.turret.convert_alpha()
        self.rect = self.turret.get_rect()
        self.image = self.turret

        self.x = 490
        self.y = 320
        self.dir = 0
        self.turnR = 5
        self.power = 0
        
        self.allSprites = allsprites
        self.playerShellPower = 60
        self.tank = playerTank
        self.enemy = prey

    def update(self):
        self.setPos()
        self.getDirection()
        self.rotate()
        
        
        
    def getDirection(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        x = (self.x-mouseX)
        y = (self.y-mouseY)
        self.dir = ((math.atan2(y, x)*(180/math.pi))*-1)+180

    def rotate(self):
        Center = self.rect.center
        self.image = pygame.transform.rotate(self.turret, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = Center

    def setPos(self):
        self.x = self.tank.rect.centerx
        self.y = self.tank.rect.centery
        self.rect.center = (self.x, self.y)




