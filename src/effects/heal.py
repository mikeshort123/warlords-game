from src.effects.effect import Effect

class Heal(Effect):

    HEALTH = 1000
    STACK_MULTIPLIER = 1.1

    def __init__(self):

        Effect.__init__(self)



    def tick(self, guy):

        guy.health += int(Heal.HEALTH * (self.stacks) ** Heal.STACK_MULTIPLIER)
        self.stacks = 0
