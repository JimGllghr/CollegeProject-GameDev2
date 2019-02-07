import pygame
pygame.init()
import math

class Explosion(pygame.sprite.Sprite):
    def __init__(self , (x,y)):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()

        self.frame = 0
        self.delay = 1
        self.pause = 0
        self.x = x
        self.y = y

        self.image = self.imgList[0]
        #self.rect = self.image.get_rect()
        """ambient = pygame.mixer.Sound(boom.wav)
        ambient.play()"""
        self.timer = 0

    def loadImages(self):
        imgMaster = pygame.image.load("explosion.png")
        imgMaster = imgMaster.convert_alpha()
        self.imgList = []
        imgSize = (125, 125)
        offset = ((0, 0), (128, 0), (256, 0), (384, 0), (512, 0),
                  (640, 0), (768, 0), (896, 0), (1024, 0),
                  (1152, 0), (1280, 0), (1408, 0), (1536, 0),
                  (1664, 0), (1792, 0), (1920, 0), (2048, 0),
                  (2176, 0), (2304, 0), (2432, 0), (2560, 0),
                  (2688, 0), (2816, 0), (2944, 0), (3072, 0),
                  (3200, 0), (3328, 0), (3456, 0), (3584, 0),
                  (3712, 0), (3840, 0), (3968, 0), (4096, 0),
                   (4224, 0)
                  )
        for i in range(32):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)

    def update(self):
        self.pause += 1
        if self.frame < (len(self.imgList)-1):
            if self.pause >= self.delay:
                self.pause = 0
                self.frame += 1
                self.image = self.imgList[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = (self.x, self.y)
        if self.frame >= (len(self.imgList)):
            self.nothing = pygame.image.load("blank.png")
            self.nothing = self.ship.convert_alpha()
        self.timer +=1
        if self.timer == 33:
            self.kill()

