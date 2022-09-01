import random

from src.utils.vector import Vector

class Chaser:

    def __init__(self, pos):

        self.allowance = 0.3
        self.target = pos.copy()


    def tick(self, pos, speed, player, grid):

        if grid.traceRay(pos, player.pos):
            self.target = player.pos.copy()

        if not self.atTarget(pos):

            return (self.target - pos).normalize(m = speed)

        return Vector()


    def atTarget(self, pos):

        return (self.target - pos).length() < self.allowance
