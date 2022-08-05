from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Slow(Effect):

    TIME = 100
    STACK_INCREASE_RATE = 1.5

    COLOUR = (100,100,255)

    TARGET = True

    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Slow.TIME:
            self.timer = 0
            self.stacks -= 1
            return

        self.timer += 1
        #guy.modified_speed *= Slow.STACK_INCREASE_RATE ** (-self.stacks)

        guy.modded_stats[ArmourStats.SPEED] *= Slow.STACK_INCREASE_RATE ** (-self.stacks)
