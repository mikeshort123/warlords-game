from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Radiant(Effect):

    TIME = 100
    MAX_DAMAGE_MULTIPLIER = 2
    STACK_INCREASE_RATE = 4

    COLOUR = (255,100,0)

    TARGET = False

    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Radiant.TIME:
            self.timer = 0
            self.stacks -= 1
            return

        self.timer += 1

        guy.modded_stats[ArmourStats.DAMAGE] *= Radiant.MAX_DAMAGE_MULTIPLIER * (1 - Radiant.STACK_INCREASE_RATE**(-self.stacks))
