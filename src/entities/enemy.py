import json,pygame,math

from src.utils.assets import Assets
from src.utils.vector import Vector
from src.entities.bullet import Bullet
from src.ais.xslider import XSlider

class Enemy:

    def __init__(self,pos,generator):

        self.pos = pos
        self.ai = XSlider(self.pos, 3, 0.1)

        self.model, self.animator = Assets.loadModel(generator.model_path)
        self.maxhealth = generator.maxhealth
        self.health = generator.maxhealth
        self.hitbox_size = generator.hitbox_size
        self.hitbox_offset = generator.hitbox_offset


    def tick(self,grid,player):


        v = self.ai.tick(self.pos)
        self.pos += v
        self.animator.setVariable("walking",not v.isZero())

        # setting this variable for all enemies is bad, fix
        self.animator.setVariable("x_vel", v.x * 64)
        self.animator.setVariable("-x_vel", -v.x * 64)

        # point arm at player
        theta = math.pi/2 + (self.pos - player.pos + Vector(40,-14) / 32).atan()
        self.animator.setVariable("pointing", -theta)

        self.animator.tick()




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
