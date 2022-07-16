import pygame

from src.tiles.tile import Tile

class Bullet:

    def __init__(self,pos,dir,colour):

        self.pos = pos
        self.dir = dir * 0.5

        self.colour = colour

        self.alive = True

    def tick(self,handler,grid):

        self.pos += self.dir

        index = (self.pos + 0.5).int()

        if Tile.getTile(grid[index.x][index.y]).solid: self.alive = False

    def render(self,renderer,cam):

        dpos = (self.pos*cam.scl).int() + (renderer.windowSize / 2).int() - (cam.pos * cam.scl).int()

        pygame.draw.circle(renderer.display,self.colour,dpos.list(),5)
