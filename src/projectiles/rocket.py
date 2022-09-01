import pygame

from src.projectiles.projectile import Projectile
from src.events.eventManager import EventManager
from src.events.eventType import EventType
from src.events.explosion import Explosion

class Rocket(Projectile):

    def render(self,renderer,cam):

        w_pos = renderer.getWorldPos(self.pos, cam)
        pygame.draw.circle(renderer.display,(0,0,0),w_pos.list(), 0.16 * renderer.max_ratio * cam.scl)
        pygame.draw.circle(renderer.display,self.element.colour,w_pos.list(), 0.14 * renderer.max_ratio * cam.scl)

    def hit_wall(self): self.explode()
    def hit_guy(self, guy): self.explode()


    def explode(self):

        EventManager.trigger_event(
            EventType.EXPLOSION,
            Explosion(
                self.pos,
                5,
                self.element.colour,
                self.damage,
                self.element,
                self.source,
                self.effects
            )
        )

        self.alive = False
