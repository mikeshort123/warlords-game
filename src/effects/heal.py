from src.effects.effect import Effect

class Heal(Effect):

    HEALTH = 1000
    STACK_MULTIPLIER = 1.1

    COLOUR = (120,255,50)

    TARGET = False

    def __init__(self, source):

        Effect.__init__(self, source)



    def tick(self, guy):

        guy.health += int(Heal.HEALTH * (self.stacks) ** Heal.STACK_MULTIPLIER)
        self.stacks = 0
