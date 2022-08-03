from src.effects.burn import Burn
from src.effects.ignition import Ignition
from src.effects.slow import Slow
from src.effects.heal import Heal
from src.effects.speed import Speed
from src.effects.poison import Poison

class Effects:

    effects = {
        "Burn" : Burn,
        "Ignition" : Ignition,
        "Slow" : Slow,
        "Heal" : Heal,
        "Speed" : Speed,
        "Poison" : Poison
    }


    @staticmethod
    def getEffectFromName(name):

        return Effects.effects[name]
