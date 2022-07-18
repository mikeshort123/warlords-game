from src.utils.vector import Vector
from src.animations.blank import Blank

class Feet(Blank):

    def __init__(self, magnitude, period):

        Blank.__init__(self)

        self.magnitude = magnitude
        self.period = period

        self.t = 0


    def tick(self, handler):

        self.t += 1

        if self.t >= self.period * 4:
            self.t = 0

        y = self.t / self.period

        if y > 1:
            y = 2 - y

        if y < -1:
            y = -2 - y

        self.offset = Vector(0,y*self.magnitude)
