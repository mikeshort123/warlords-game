from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Speed(Effect):

    TIME = 100
    MAX_SPEED_MULTIPLIER = 2
    STACK_INCREASE_RATE = 4

    COLOUR = (100,50,180)

    TARGET = False

    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Speed.TIME:
            self.timer = 0
            self.stacks -= 1
            return

        self.timer += 1
        #guy.modified_speed *= Speed.MAX_SPEED_MULTIPLIER * (1 - Speed.STACK_INCREASE_RATE**(-self.stacks))

        guy.modded_stats[ArmourStats.SPEED] *= Speed.MAX_SPEED_MULTIPLIER * (1 - Speed.STACK_INCREASE_RATE**(-self.stacks))
