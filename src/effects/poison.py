from src.effects.effect import Effect

class Poison(Effect):

    TOTAL_TICKS = 10
    TICK_TIME_DELTA = 10
    DAMAGE = 100

    def __init__(self):

        Effect.__init__(self)

        self.tick_timer = 0
        self.tick_counter = 0



    def tick(self, guy):

        if self.tick_timer < Poison.TICK_TIME_DELTA:
            self.tick_timer += 1
            return

        self.tick_timer = 0
        self.tick_counter += 1

        guy.health -= Poison.DAMAGE * self.stacks

        if self.tick_counter >= Poison.TOTAL_TICKS:
            self.stacks -= 1
            self.tick_counter = 0
