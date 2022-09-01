import pygame

class Rocket:

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
        if grid.getSolid(index.x,index.y): self.alive = False

        for entity in entities: # check entity collision
            if entity.inHitbox(self.pos):

                self.registerHit(entity)
                return


    def render(self,renderer,cam):

        w_pos = renderer.getWorldPos(self.pos, cam)
        pygame.draw.circle(renderer.display,(0,0,0),w_pos.list(), 0.16 * renderer.max_ratio * cam.scl)
        pygame.draw.circle(renderer.display,self.element.colour,w_pos.list(), 0.14 * renderer.max_ratio * cam.scl)


    def registerHit(self, entity):

        entity.applyDamage(self.damage, self.element)

        for (EffectType, procs) in self.effects:

            if EffectType.TARGET:
                entity.applyEffect(EffectType, procs) # debuff, apply to target
            else:
                self.source.applyEffect(EffectType, procs) # buff, apply to source

        self.alive = False
