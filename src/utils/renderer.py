import pygame
from src.utils.vector import Vector

class Renderer():

    def __init__(self,display):

        self.display = display
        self.windowSize = Vector(self.display.get_width(),self.display.get_height())

    def drawImage(self, img, x, y):

        self.display.blit(img, (x,y))

    def drawCamImage(self,img,pos,size,cam):

        dsize = size * cam.scl
        dpos = (pos*cam.scl).int() + ((self.windowSize - dsize) / 2).int() - (cam.pos * cam.scl).int()

        img = pygame.transform.scale(img, dsize.int().list())

        self.display.blit(img, dpos.list())

    def drawAlphaBackground(self,colour,alpha):

        s = pygame.Surface(self.display.get_size())
        s.set_alpha(alpha)
        s.fill(colour)
        self.display.blit(s,(0,0))
