import pygame
import random

class ControlData:
    def __init__(self):
        self.moveX = 0
        self.moveY = 0

class Mine(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        randomNo = random.randint(1,2)

        self.screen = screen
        self.image = pygame.image.load("Mine.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        randomY = random.randint(1,640)
        randomX = random.randint(1,920)
        self.rect.center = (randomX, randomY)

        'Position the sprite'
        self.x = randomX
        self.y = randomY

        pdr = ControlData()
        pdr.moveX = 4

        pdl = ControlData()
        pdl.moveX = -4

        pdd = ControlData()
        pdd.moveY = 4

        pdu = ControlData()
        pdu.moveY = -4

        if randomNo == 1:
            self.pattern = [pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr,
                            pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd,
                            pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl,
                            pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu]
        if randomNo == 2:
            self.pattern = [pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr,
                            pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd,
                            pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl,
                            pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd, pdd]
        if randomNo == 3:
            self.pattern = [pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr, pdr,
                            pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu,
                            pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl, pdl,
                            pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu, pdu]
        self.patternIndex = 0


    def update(self):

        'Update the sprite position using the array of pattern data'

        cd = self.pattern[self.patternIndex]
        self.x += cd.moveX
        self.y += cd.moveY


        'Increment the patternIndex so that we move to the next piece of pattern data'
        self.patternIndex += 1

        'Reset the patternIndex if we are at the end of the array'
        if self.patternIndex >= len(self.pattern):
            self.patternIndex = 0

        if self.x > self.screen.get_width():
            self.kill()
        if self.x < 0:
            selfkill()
        if self.y > self.screen.get_height():
            self.kill()
        if self.y < 0:
            self.kill()

        self.rect.center = (self.x, self.y)
