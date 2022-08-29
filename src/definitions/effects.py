from src.effects.burn import Burn
from src.effects.ignition import Ignition
from src.effects.radiant import Radiant
from src.effects.slow import Slow
from src.effects.bolstered import Bolstered
from src.effects.heal import Heal
from src.effects.empowered import Empowered
from src.effects.speed import Speed
from src.effects.miasma import Miasma

class Effects:

    effects = {
        "Burn" : Burn,
        "Ignition" : Ignition,
        "Radiant" : Radiant,

        "Slow" : Slow,
        "Bolstered" : Bolstered,

        "Heal" : Heal,
        "Empowered" : Empowered,

        "Speed" : Speed,
        
        "Miasma" : Miasma
    }


    @staticmethod
    def getEffectFromName(name):

        return Effects.effects[name]
