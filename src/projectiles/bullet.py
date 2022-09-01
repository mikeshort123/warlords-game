import pygame

from src.projectiles.projectile import Projectile

class Bullet(Projectile):

    def render(self,renderer,cam):

        w_pos = renderer.getWorldPos(self.pos, cam)
        pygame.draw.circle(renderer.display,(0,0,0),w_pos.list(), 0.08 * renderer.max_ratio * cam.scl)
        pygame.draw.circle(renderer.display,self.element.colour,w_pos.list(), 0.06 * renderer.max_ratio * cam.scl)

    def hit_guy(self, guy):

        guy.applyDamage(self.damage, self.element)

        for (EffectType, procs) in self.effects():

            if EffectType.TARGET:
                guy.applyEffect(EffectType, procs, self.source) # debuff, apply to target
            else:
                self.source.applyEffect(EffectType, procs, self.source) # buff, apply to source
