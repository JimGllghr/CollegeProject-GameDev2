import pygame, math

class Shell(pygame.sprite.Sprite):
    def __init__(self, screen, (x, y), direction, player, scoreboard):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.turret = pygame.image.load("shell.png")
        self.turret = self.turret.convert_alpha()
        self.rect = self.turret.get_rect()
        self.image = self.turret

        self.x = x
        self.y = y
        self.speed = 6
        self.dir = direction
        self.prey = player
        self.score = scoreboard
        self.preyGroup = pygame.sprite.GroupSingle(sprite=self.prey)

    def update(self):
        self.calcVector()
        self.setPos()
        self.rotate()
        self.rect.center = (self.x, self.y)

        playerHit = pygame.sprite.spritecollide(self, self.preyGroup, False)
        if playerHit:
            self.kill()
            self.score.health -=20

    def rotate(self):
        Center = self.rect.center
        self.image = pygame.transform.rotate(self.turret, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = Center

    def setPos(self):
        self.x += self.dx
        self.y += self.dy

    def calcVector(self):
        radians = self.dir * math.pi / 180
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1
        self.dx += self.dx
        self.dy += self.dy



