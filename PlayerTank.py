import pygame, math

class PlayerTank(pygame.sprite.Sprite):
    def __init__(self, screen, (x, y), AllSprites, prey):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.tank = pygame.image.load("playerTank.png")
        self.tank = self.tank.convert_alpha()
        self.rect = self.tank.get_rect()
        self.image = self.tank
        self.rect.center = (x, y)

        self.x = y
        self.y = x
        self.dx = 0
        self.dy = 0
        self.dir = 90
        self.turnR = 2
        self.momentom = 0
        self.maxspeed = 10
        self.allSprites = AllSprites
        self.px = 0 
        self.py = 0
        
        
    def update(self):
        self.checkKeys()
        self.calcVector()
        self.rotate()
        self.setPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)

    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.dir -= self.turnR
            if self.dir < 0:
                self.dir = 360 - self.turnR
        if keys[pygame.K_LEFT]:
            self.dir += self.turnR
            if self.dir > 360:
                self.dir = self.turnR
        if (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            if keys[pygame.K_UP]:
                if self.momentom>-3.5:
                    self.momentom += -.1
            if keys[pygame.K_DOWN]:
                if self.momentom<3.5:
                 self.momentom += .1
        else:
            if (self.momentom<0):
                self.momentom += .1
            if (self.momentom>0):
                self.momentom += -.1
        
    def rotate(self):
        Center = self.rect.center
        self.image = pygame.transform.rotate(self.tank, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = Center

    def calcVector(self):
        radians = self.dir * math.pi / 180
        self.dx = self.momentom * math.cos(radians)
        self.dy = self.momentom * math.sin(radians)
        self.dy *= -1
        self.dx += self.dx
        self.dy += self.dy

    def setPos(self):
        self.x += self.dx
        self.y += self.dy

    def checkBounds(self):
        screen = self.screen
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = screen.get_width()
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = screen.get_height()
