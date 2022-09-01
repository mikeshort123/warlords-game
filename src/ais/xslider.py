import random

from src.utils.vector import Vector

class XSlider:

    def __init__(self,pos,reach):

        self.centre = pos.x
        self.left = pos.x - reach
        self.right = pos.x + reach

        self.moving = False

        self.target = self.centre
        self.allowance = 0.3


    def tick(self, pos, speed, player, grid):

        if self.atTarget(pos):
            r = random.randint(0,100)

            if r == 0: self.target = self.centre
            if r == 1: self.target = self.left
            if r == 2: self.target = self.right

            return Vector()

        else:
            d = speed if pos.x < self.target else -speed
            return Vector(d,0)


    def atTarget(self, pos):

        return abs(self.target - pos.x) < self.allowance
