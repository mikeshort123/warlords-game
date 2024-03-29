import json,pygame,math

from src.utils.assets import Assets
from src.utils.soundManager import SoundManager
from src.utils.vector import Vector
from src.entities.bullet import Bullet
from src.ais.xslider import XSlider
from src.definitions.element import Element
from src.utils.hitbox import Hitbox

class Enemy:

    def __init__(self,pos,generator):

        self.pos = pos
        self.speed = 0.1
        self.ai = XSlider(self.pos, 3)

        self.effects = {}

        self.model, self.animator = Assets.loadModel(generator.model_path)
        self.maxhealth = generator.maxhealth
        self.health = generator.maxhealth
        self.hitbox_size = generator.hitbox_size
        self.hitbox_offset = generator.hitbox_offset

        self.hitbox = Hitbox.fromVectors(self.hitbox_offset, self.hitbox_size)

        self.damage_sound = Assets.loadSound("res/sounds/pop.wav")


    def tick(self,grid,player):

        self.modified_speed = self.speed

        for name, effect in list(self.effects.items()): # had to convert to list, as modifying a dict mid loop would upset python

            effect.tick(self)
            if effect.stacks == 0:
                self.effects.pop(name)


        v = self.ai.tick(self.pos, self.modified_speed)
        self.pos += v
        self.animator.setVariable("walking", not v.isZero())

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

        for i, effect_type in enumerate(self.effects):

            pygame.draw.rect(screen,effect_type.COLOUR,(dpos.x + 25*i,dpos.y-25,20,20))


    def applyDamage(self, damage, element):

        self.health -= damage

        SoundManager.playSound(self.damage_sound)


    def applyEffect(self, EffectType, amount):

        if EffectType not in self.effects:
            self.effects[EffectType] = EffectType()

        self.effects[EffectType].addStacks(amount)


    def getElementalEffects(self, element):

        return [] # for now enemies dont need to apply effects, but that will likely change


    def inHitbox(self,pos):

        return self.hitbox.isInside(pos - self.pos)
