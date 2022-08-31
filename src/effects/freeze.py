from src.effects.effect import Effect
from src.definitions.armourStats import ArmourStats

class Freeze(Effect):

    DELAY = 60
    DAMAGE = 1000
    STACK_MULTIPLIER = 1.1

    COLOUR = (0,150,255)

    TARGET = True

    def __init__(self):

        Effect.__init__(self)

        self.delay_timer = 0


    def tick(self, guy):

        guy.modded_stats[ArmourStats.SPEED] = 0

        if self.delay_timer < Freeze.DELAY:
            self.delay_timer += 1
            return

        guy.applyDamage(Freeze.DAMAGE * (self.stacks) ** Freeze.STACK_MULTIPLIER, None)

        self.stacks = 0
