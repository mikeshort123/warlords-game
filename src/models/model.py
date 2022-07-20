import json,pygame,math

from src.utils.vector import Vector

class Model():

    def __init__(self,img,size,centre,offset):

        self.img = img
        self.size = size
        self.centre = centre
        self.offset = offset



    def render(self, renderer, pos, cam, d = None, theta = 0, override = False, untoffset = None, temp = None):


        if temp:
            untoffset = temp.offset
            theta = temp.theta

        dsize = self.size * cam.scl
        img = pygame.transform.scale(self.img, dsize.int().list())
        centre = self.centre.copy()
        if d:
            if override:
                centre = d.copy()
            else:
                centre += d

        if theta != 0:
            img = pygame.transform.rotate(img, 180*theta / math.pi)
            centre = centre.rotate(theta)
        if untoffset:
            centre += untoffset

        centre += self.offset

        dpos = ((pos+centre)*cam.scl) + ((renderer.windowSize - Vector(img.get_size())) / 2) - (cam.pos * cam.scl)



        renderer.drawImage(img, int(dpos.x), int(dpos.y))
