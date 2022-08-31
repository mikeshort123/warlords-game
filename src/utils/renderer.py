import pygame
from src.utils.vector import Vector

class Renderer():

    renderer = None

    def __init__(self, w, h):

        self.w = w
        self.h = h
        self.resize_screen(w, h)

        Renderer.renderer = self

    def resize_screen(self, w, h):
        self.display = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        self.windowSize = Vector(self.display.get_width(),self.display.get_height())

        self.min_ratio = min(w / self.w, h / self.h)
        self.max_ratio = max(w / self.w, h / self.h)

        self.x_offset = (w - self.w * self.min_ratio) / 2
        self.y_offset = (h - self.h * self.min_ratio) / 2

    def drawImage(self, img, x, y):

        self.display.blit(img, (x,y))

    def drawUIImage(self, img, x, y):

        t_img = pygame.transform.scale(img, (img.get_width() * self.min_ratio, img.get_height() * self.min_ratio))
        t_pos = (
            self.x_offset + x * self.min_ratio,
            self.y_offset + y * self.min_ratio
        )
        self.display.blit(t_img, t_pos)

    def drawWorldImage(self, img, pos, size, cam):

        w_pos = self.getWorldPos(pos, cam)
        w_size = self.getWorldSize(size, cam)

        t_img = pygame.transform.scale(img, w_size.list())

        self.display.blit(t_img, (w_pos - w_size/2).int().list())

    def getWorldPos(self, pos, cam):
        return (pos - cam.pos) * self.max_ratio * cam.scl + self.windowSize / 2

    def getWorldSize(self, size, cam):
        return size * self.max_ratio * cam.scl + 1

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
