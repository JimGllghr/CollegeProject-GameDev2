import pygame, math

from shell import Shell

class enemyTurretA(pygame.sprite.Sprite):
    def __init__(self, screen, playerTank, ownTank, scoreboard, allsprites):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.turret = pygame.image.load("enemyTurretA.png")
        self.turret = self.turret.convert_alpha()
        self.rect = self.turret.get_rect()
        self.image = self.turret

        self.x = 490
        self.y = 320
        self.dir = 0
        self.turnR = 5
        self.power = 0
        
        self.tank = ownTank
        self.preyTank = playerTank
        self.Screen = screen
        self.score = scoreboard
        self.allSprites = allsprites

    def update(self):
        self.setPos()
        if self.tank.mag<400:
            self.getDirection()
        self.rotate()
        self.rect.center = (self.x, self.y)
        self.power +=1
        
        self.checkCanFire()

    def getDirection(self):
        x = (self.x-self.preyTank.rect.centerx)
        y = (self.y-self.preyTank.rect.centery)

        self.pdir = ((math.atan2(y, x)*(180/math.pi))*-1)+180
        if self.dir>self.pdir:
            self.dir -= self.turnR
            if self.dir < 0:
                self.dir = 360 - self.turnR
        if self.dir<self.pdir:
            self.dir += self.turnR
            if self.dir > 360:
                self.dir = self.turnR

    def checkCanFire(self):
        if self.power>90:
            if self.tank.mag<400:
                shell = Shell(self.Screen, (self.x, self.y), self.dir, self.preyTank, self.score)
                self.allSprites.add(shell)
                self.power = 0
        

    def rotate(self):
        Center = self.rect.center
        self.image = pygame.transform.rotate(self.turret, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = Center

    def setPos(self):
        self.x = self.tank.rect.centerx
        self.y = self.tank.rect.centery




