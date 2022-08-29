from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Bolstered(Effect):

    TIME = 100
    MAX_RESIST_MULTIPLIER = 2
    STACK_INCREASE_RATE = 4

    COLOUR = (0,100,255)

    TARGET = False

    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Bolstered.TIME:
            self.timer = 0
            self.stacks -= 1
            return

        self.timer += 1

        guy.modded_stats[ArmourStats.DEFENCE] *= Bolstered.MAX_RESIST_MULTIPLIER * (1 - Bolstered.STACK_INCREASE_RATE**(-self.stacks))
