from src.utils.assets import Assets
from src.utils.soundManager import SoundManager

class Dude:

    def __init__(self, pos):

        self.pos = pos

        self.maxhealth
        self.health
        self.effects = {}
        self.damage_sound = Assets.loadSound("res/sounds/pop.wav")

    def tick(self, handler): return
    def render(self, renderer): return

    def applyDamage(self, damage, element):

        self.health -= damage

        SoundManager.playSound(self.damage_sound)


    def applyEffect(self, EffectType, amount):

        if EffectType not in self.effects:
            self.effects[EffectType] = EffectType()

        self.effects[EffectType].addStacks(amount)

    def getElementalEffects(self, element): return []
