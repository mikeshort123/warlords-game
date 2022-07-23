from src.effects.effect import Effect

class Ignition(Effect):

    DELAY = 40
    DAMAGE = 1000
    STACK_MULTIPLIER = 1.1

    def __init__(self):

        Effect.__init__(self)

        self.delay_timer = 0


    def tick(self, guy):

        if self.delay_timer < Ignition.DELAY:
            self.delay_timer += 1
            return

        guy.health -= int(Ignition.DAMAGE * (self.stacks) ** Ignition.STACK_MULTIPLIER)

        self.stacks = 0
