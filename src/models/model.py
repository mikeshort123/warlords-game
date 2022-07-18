import json,pygame,math

from src.utils.vector import Vector

class Model():

    def __init__(self,img,size,offset):

        self.img = img
        self.size = size
        self.offset = offset



    def render(self, renderer, pos, cam, d = None, theta = 0, override = False, untoffset = None, temp = None):


        if temp:
            untoffset = temp.offset
            theta = temp.theta

        dsize = self.size * cam.scl
        img = pygame.transform.scale(self.img, dsize.int().list())
        offset = self.offset.copy()
        if d:
            if override:
                offset = d.copy()
            else:
                offset += d

        if theta != 0:
            img = pygame.transform.rotate(img, 180*theta / math.pi)
            offset = offset.rotate(theta)
        if untoffset:
            offset += untoffset

        dpos = ((pos+offset)*cam.scl) + ((renderer.windowSize - Vector(img.get_size())) / 2) - (cam.pos * cam.scl)



        renderer.drawImage(img, int(dpos.x), int(dpos.y))
