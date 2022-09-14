import pygame

from src.projectiles.projectile import Projectile

class Melee(Projectile):

    def __init__(self, pos, dir, element, source, damage, effects):

        super().__init__(pos, dir, element, source, damage, effects)
        self.length = 4
        self.start = pos.copy()
        self.hit = []

    def render(self,renderer,cam):

        w_pos = renderer.getWorldPos(self.pos, cam)
        start_pos = renderer.getWorldPos(self.start, cam)
        pygame.draw.line(renderer.display,self.element.colour,w_pos.list(), start_pos.list(), width = int(0.48 * renderer.max_ratio * cam.scl))

    def tick(self,grid,entities):

        self.pos += self.dir # move bullet

        if (self.pos-self.start).length() >= self.length:
            self.alive = False

        index = (self.pos + 0.5).int() # check wall collision
        if grid.getSolid(index.x,index.y):
            self.hit_wall()
            self.alive = False

        for entity in entities: # check entity collision
            if entity.inHitbox(self.pos):

                self.hit_guy(entity)


    def hit_guy(self, guy):

        if guy in self.hit: # avoid hitting enemies more than once
            return

        self.hit.append(guy)

        guy.applyDamage(self.damage, self.element)

        for (EffectType, procs) in self.effects():

            if EffectType.TARGET:
                guy.applyEffect(EffectType, procs, self.source) # debuff, apply to target
            else:
                self.source.applyEffect(EffectType, procs, self.source) # buff, apply to source
