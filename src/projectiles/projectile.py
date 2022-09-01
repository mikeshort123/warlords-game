import pygame

class Projectile:

    def __init__(self, pos, dir, element, source, damage, effects):

        self.pos = pos
        self.dir = dir * 0.5

        self.element = element

        self.source = source
        self.damage = damage
        self.effects = effects

        self.alive = True



    def tick(self,grid,entities):

        self.pos += self.dir # move bullet

        index = (self.pos + 0.5).int() # check wall collision
        if grid.getSolid(index.x,index.y):
            self.hit_wall()
            self.alive = False

        for entity in entities: # check entity collision
            if entity.inHitbox(self.pos):

                self.hit_guy(entity)
                self.alive = False


    def render(self,renderer,cam): return

    def hit_wall(self): return
    def hit_guy(self, guy): return
