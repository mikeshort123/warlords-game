from src.effects.effect import Effect
from src.events.eventManager import EventManager
from src.events.eventType import EventType
from src.events.explosion import Explosion

class Ignition(Effect):

    DELAY = 40
    DAMAGE = 1000
    STACK_MULTIPLIER = 1.1

    COLOUR = (255,150,0)

    TARGET = True

    def __init__(self, source):

        Effect.__init__(self, source)

        self.delay_timer = 0


    def tick(self, guy):

        if self.delay_timer < Ignition.DELAY:
            self.delay_timer += 1
            return


        EventManager.trigger_event(
            EventType.EXPLOSION,
            Explosion(
                guy.pos.copy(),
                5,
                Ignition.COLOUR,
                Ignition.DAMAGE * (self.stacks) ** Ignition.STACK_MULTIPLIER,
                None,
                self.source,
                self.genEffects
            )
        )

        self.stacks = 0

    def genEffects(self):
        return []
