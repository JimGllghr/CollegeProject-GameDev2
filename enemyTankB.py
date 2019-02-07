import pygame, math

class EnemyTank2(pygame.sprite.Sprite):
    def __init__(self, screen, (x, y), crate, scoreboard):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.tank = pygame.image.load("truck.png")
        self.tank = self.tank.convert_alpha()
        self.rect = self.tank.get_rect()
        self.image = self.tank
        self.rect.center = (x, y)
        self.patrolStep = 1

        self.x = y
        self.y = x
        self.dx = 0
        self.dy = 0
        self.dir = 0
        self.pDir = 0
        self.turnR = 2
        self.momentom = 0
        self.maxspeed = 10
        self.alive = True
        self.health = 30
        self.respawn = 0

        self.prey = crate
        self.score = scoreboard
        self.enemySprite = pygame.sprite.GroupSingle(sprite=self.prey)

    def update(self):
        self.getMag()
        self.move()
        self.calcVector()
        self.rotate()
        self.setPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)
        self.checkAlive()
        self.checkCollision()
        if self.respawn == 1:
            self.x = 200
            self.y = 200
            self.respawn -= 1

    def checkAlive(self):
        if self.health<=0:
            self.alive = False
            self.health = 20
            self.reset()

    def getMag(self):
        rangeToCloseX = self.prey.x - self.x
        rangeToCloseY = self.prey.y - self.y
        self.mag = math.sqrt((rangeToCloseX ** 2)+(rangeToCloseY ** 2))

    def move(self):
        x = (self.prey.x-self.x)
        y = (self.prey.y-self.y)
        self.preyDir = ((math.atan2(y, x)*(180/math.pi))*-1)+180

        chasing = self.mag<400
        patroling = self.mag>400
        accelerating = self.mag>100
        
        if chasing:
            if (self.dir>self.preyDir):
                    self.turnRight()
            if (self.dir<self.preyDir):
                    self.turnLeft()

        if patroling:
            if self.momentom>-3:
                 self.momentom += -.1
            self.patrol()

        elif accelerating:
             if self.momentom>-3:
                 self.momentom += -.1

    def turnRight(self):
        self.dir -= self.turnR
        if self.dir < 0:
            self.dir = 360 - self.turnR

    def turnLeft(self):
        self.dir += self.turnR
        if self.dir > 360:
            self.dir = self.turnR

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
    
          
    def patrol(self):
        self.patrolStep+=1
        if self.patrolStep>91 and self.patrolStep<180:
            self.turnRight()
        if self.patrolStep>270 and self.patrolStep<360:
            self.turnLeft()
        if self.patrolStep>450:
            self.patrolStep = 1

    def checkCollision(self):
        collectPackage = pygame.sprite.spritecollide(self, self.enemySprite, False)
        if collectPackage:
            self.prey.reset()
            self.score.health -= 2
    
    def reset(self):
        self.x = 3000
        self.y = 4000
        self.respawn = 620