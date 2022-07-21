import pygame


class Bullet:

    def __init__(self,pos,dir,source):

        self.pos = pos
        self.dir = dir * 0.5

        self.source = source

        self.colour = source.element.colour

        self.alive = True

    def tick(self,grid,entities):

        self.pos += self.dir # move bullet

        index = (self.pos + 0.5).int() # check wall collision
        if grid.getSolid(index.x,index.y): self.alive = False

        for entity in entities: # check entity collision
            if entity.inHitbox(self.pos):
                damage, element, procs = self.source.generateDamageProfile()
                entity.health -= damage
                print(damage, element, procs)
                self.alive = False

    def render(self,renderer,cam):

        dpos = (self.pos*cam.scl).int() + (renderer.windowSize / 2).int() - (cam.pos * cam.scl).int()

        pygame.draw.circle(renderer.display,(0,0,0),dpos.list(),5)
        pygame.draw.circle(renderer.display,self.colour,dpos.list(),4)
