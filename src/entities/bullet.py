import pygame

from src.definitions.element import Element
from src.definitions.armourStats import ArmourStats


class Bullet:

    def __init__(self, pos, dir, colour, source, damageProfileGenerator):

        self.pos = pos
        self.dir = dir * 0.5

        self.source = source
        self.damageProfileGenerator = damageProfileGenerator

        self.colour = colour

        self.alive = True



    def tick(self,grid,entities):

        self.pos += self.dir # move bullet

        index = (self.pos + 0.5).int() # check wall collision
        if grid.getSolid(index.x,index.y): self.alive = False

        for entity in entities: # check entity collision
            if entity.inHitbox(self.pos):

                self.registerHit(entity)
                return


    def render(self,renderer,cam):

        dpos = (self.pos*cam.scl).int() + (renderer.windowSize / 2).int() - (cam.pos * cam.scl).int()

        pygame.draw.circle(renderer.display,(0,0,0),dpos.list(),5)
        pygame.draw.circle(renderer.display,self.colour,dpos.list(),4)


    def registerHit(self, entity):

        damage, element, procs = self.damageProfileGenerator()
        entity.applyDamage(damage * self.source.modded_stats[ArmourStats.DAMAGE], element)

        if procs >= 1:

            effects = self.source.getElementalEffects(element)

            for EffectType in effects:

                if EffectType.TARGET:
                    entity.applyEffect(EffectType, procs) # debuff, apply to target
                else:
                    self.source.applyEffect(EffectType, procs) # buff, apply to source

        self.alive = False
