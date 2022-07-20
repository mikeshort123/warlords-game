import json,pygame
from src.utils.assets import Assets
from src.utils.vector import Vector
from src.entities.bullet import Bullet
from src.animations.animationController import AnimationController

class Enemy:

    def __init__(self, fn, pos):

        with open(fn) as f:
            data = json.load(f)

        model_path = data["model"]

        self.model, self.animator = Assets.loadModel(model_path)

        self.pos = pos

        self.alive = True

        self.maxhealth = data["health"]
        self.health = self.maxhealth

        self.hitbox_size = Vector(data["hitbox_size"]) / self.model.scale
        self.hitbox_offset = (Vector(data["hitbox_offset"]) / self.model.scale) - (self.hitbox_size / 2)


    def tick(self,handler,grid,entities,player):

        #for _, part in self.animations.items():
        #    part.tick(handler)

        self.animator.tick()

        for entity in entities:
            if isinstance(entity,Bullet):
                if self.inHitbox(entity.pos):
                    self.health -= 100
                    entity.alive = False

        if self.health <= 0:
            self.alive = False

        s = handler.getKeyPressed("START")
        self.animator.setVariable("walking",s)


    def render(self,renderer,cam):

        self.model.render(renderer,self.pos,cam,self.animator)

        dpos = (self.pos*cam.scl).int() + (renderer.windowSize / 2).int() - (cam.pos * cam.scl).int() - Vector(50,55)

        screen = renderer.display
        pygame.draw.rect(screen,(0,0,0),(dpos.x,dpos.y,100,10))
        pygame.draw.rect(screen,(255,0,0),(dpos.x,dpos.y,100*self.health // self.maxhealth,10))


    def inHitbox(self,pos):

        px,py = pos.list()
        ax,ay = (self.pos + self.hitbox_offset).list()
        bx,by = ax + self.hitbox_size.x, ay + self.hitbox_size.y

        return px >= ax and px <= bx and py >= ay and py <= by
