from src.effects.effect import Effect

class Ignition(Effect):

    DELAY = 40
    DAMAGE = 1000
    STACK_MULTIPLIER = 1.1

    COLOUR = (255,150,0)

    TARGET = True

    def __init__(self):

        Effect.__init__(self)

        self.delay_timer = 0


    def tick(self, guy):

        if self.delay_timer < Ignition.DELAY:
            self.delay_timer += 1
            return

        guy.applyDamage(Ignition.DAMAGE * (self.stacks) ** Ignition.STACK_MULTIPLIER, None)

        self.stacks = 0
