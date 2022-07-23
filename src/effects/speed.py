from src.effects.effect import Effect
from src.definitions.element import Element

class Speed(Effect):

    TIME = 100
    SPEED_MULTIPLIER = 1.4
    STACK_MULTIPLIER = 1.1

    COLOUR = (100,50,180)

    TARGET = False

    def __init__(self):

        Effect.__init__(self)

        self.timer = 0



    def tick(self, guy):

        if self.timer >= Speed.TIME:
            self.stacks -= 1
            return

        self.timer += 1
        guy.modified_speed *= Speed.SPEED_MULTIPLIER ** (self.stacks ** Speed.STACK_MULTIPLIER)
