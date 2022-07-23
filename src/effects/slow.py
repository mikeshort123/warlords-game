from src.effects.effect import Effect

class Slow(Effect):

    TIME = 100
    SPEED_MULTIPLIER = 0.7
    STACK_MULTIPLIER = 1.1


    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Slow.TIME:
            self.stacks -= 1
            return

        self.timer += 1
        guy.modified_speed *= Slow.SPEED_MULTIPLIER ** (self.stacks ** Slow.STACK_MULTIPLIER)
