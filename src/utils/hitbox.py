

class Hitbox:

    def __init__(self,x,y,w,h):

        self.ax = x
        self.ay = y
        self.bx = self.ax + w
        self.by = self.ay + h


    def isInside(self, pos):

        return pos.x >= self.ax and pos.x <= self.bx and pos.y >= self.ay and pos.y <= self.by


    @staticmethod
    def fromVectors(pos,size):
        return Hitbox(pos.x,pos.y,size.x,size.y)
