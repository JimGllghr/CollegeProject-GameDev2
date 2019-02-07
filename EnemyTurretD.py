import pygame, math

from shell import Shell

class enemyTurretD(pygame.sprite.Sprite):
    def __init__(self, screen, playerTank, ownTank, scoreboard, allsprites):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.turret = pygame.image.load("tankturretb.png")
        self.turret = self.turret.convert_alpha()
        self.rect = self.turret.get_rect()
        self.image = self.turret

        self.x = 490
        self.y = 320
        self.dir = 0
        self.turnR = 5
        self.power = 0
        self.mag = 0
        self.pSpeed = 0
        self.pdx = 0
        self.pdy = 0
        self.z = 1.0

        self.tank = ownTank
        self.preyTank = playerTank
        self.Screen = screen
        self.score = scoreboard
        self.allSprites = allsprites

    def update(self):
        self.getMag()
        self.setPos()
        #if self.tank.mag<1000:
        self.getDirection()
        self.rotate()
        self.rect.center = (self.x, self.y)
        self.power +=1
        self.checkCanFire()

    def drawVector(self, screen, (startX, startY), (vecX, vecY), scale, colour):
        toPos = [startX + vecX * scale, startY + vecY * scale]
        pygame.draw.line(screen, colour, [startX, startY], toPos, 2)

    def getMag(self):
        rangeToCloseX = self.preyTank.x - self.x
        rangeToCloseY = self.preyTank.y - self.y
        self.mag = math.sqrt((rangeToCloseX ** 2)+(rangeToCloseY ** 2))

    def getDirection(self):
        self.z  = 0.0
        self.px = self.preyTank.px
        self.py = self.preyTank.py
        self.pdx = self.preyTank.dx
        self.pdy = self.preyTank.dy
        if self.mag>150:
            if self.preyTank.momentom!=0:
                self.z = (self.mag/self.preyTank.momentom)*0.75
            self.px += self.z
            self.py += self.z

            (self.px, self.py) = [self.preyTank.x + self.pdx * 50.0, self.preyTank.y + self.pdy * 50.0]
            x = (self.preyTank.x-self.px)
            y = (self.preyTank.y-self.py)

        else:
             x = (self.x-self.preyTank.rect.centerx)
             y = (self.y-self.preyTank.rect.centery)

        

        self.pdir = ((math.atan2(y, x)*(180/math.pi))*-1)+180
        self.pdir = int(round(self.pdir))
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
                if self.dir == self.pdir:
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




