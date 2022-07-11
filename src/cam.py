from src.utils.vector import Vector

class Cam():

    def __init__(self,x,y):

        self.pos = Vector(x,y)
        self.scl = 64


    def moveTo(self,e):

        self.pos = e.pos.copy()

    def moveBy(self,v):

        self.pos += v
