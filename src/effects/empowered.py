from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Empowered(Effect):

    TIME = 100
    MAX_DAMAGE_MULTIPLIER = 2
    STACK_INCREASE_RATE = 4

    COLOUR = (255,150,0)

    TARGET = False

    def __init__(self, source):

        Effect.__init__(self, source)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Empowered.TIME:
            self.timer = 0
            self.stacks -= 1
            return

        self.timer += 1

        guy.modded_stats[ArmourStats.DAMAGE] *= Empowered.MAX_DAMAGE_MULTIPLIER * (1 - Empowered.STACK_INCREASE_RATE**(-self.stacks))
