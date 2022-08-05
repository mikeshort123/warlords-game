from src.utils.assets import Assets
from src.utils.soundManager import SoundManager
from src.definitions.armourStats import ArmourStats

class Dude:

    def __init__(self, pos):

        self.pos = pos

        self.maxhealth : float
        self.health : float
        self.effects = {}
        self.damage_sound = Assets.loadSound("res/sounds/pop.wav")

    def tick(self):

        self.modded_stats = {
            ArmourStats.SPEED : self.speed
        }

        for name, effect in list(self.effects.items()):

            effect.tick(self)
            if effect.stacks == 0:
                self.effects.pop(name)


    def render(self, renderer): return

    def applyDamage(self, damage, element):

        self.health -= damage

        SoundManager.playSound(self.damage_sound)


    def applyEffect(self, EffectType, amount):

        if EffectType not in self.effects:
            self.effects[EffectType] = EffectType()

        self.effects[EffectType].addStacks(amount)

    def getElementalEffects(self, element): return []
