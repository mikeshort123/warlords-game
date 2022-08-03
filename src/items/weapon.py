import json

from src.items.fullauto import Fullauto
from src.items.semiauto import Semiauto
from src.models.weaponModel import WeaponModel
from src.definitions.weaponStats import WeaponStats

class Weapon:

    def __init__(self, wielder, item):

        self.wielder = wielder
        self.model = WeaponModel(item.model_path)

        self.mods = item.mods

        # unpack weapon stats and data
            # maybe ill get rid of the file read at some point who knows
        weapon_type_filepath = item.frame_data["type"]
        weapon_subtype_name = item.frame_data["subtype"]

        with open(weapon_type_filepath) as f:
            weapon_type_data = json.load(f)

        frame_name_reference = {
            "gun-auto" : Fullauto,
            "gun-semiauto" : Semiauto
        }

        Trigger_type = frame_name_reference[weapon_type_data["type"]]
        weapon_subtype_stats = weapon_type_data["subtypes"][weapon_subtype_name]

        # use stats to set up weapons
        self.trigger = Trigger_type()

        self.element = item.element

        self.stats = {
            WeaponStats.DAMAGE : weapon_subtype_stats["damage"],
            WeaponStats.FIRERATE : 3600 // weapon_subtype_stats["firerate"],
            WeaponStats.ELEMENTAL_CHANCE : item.stats["element_chance"]
        }

        self.status_counter = 0


    def tick(self, handler, bulletGenerator):
        if self.trigger.tick(handler, self.getStat(WeaponStats.FIRERATE)):
            bulletGenerator(handler, self.element.colour, self.wielder, self.generateDamageProfile)


    def getStat(self,stat):

        val = self.stats[stat]

        for mod in self.mods:
            if mod and mod.function["type"] == "INCREASE_STAT" and stat == WeaponStats(mod.function["stat"]):
                val *= mod.function["scalar"]

        return val


    def generateDamageProfile(self):

        self.status_counter += self.getStat(WeaponStats.ELEMENTAL_CHANCE)
        procs = int(self.status_counter)
        self.status_counter %= 1

        return self.getStat(WeaponStats.DAMAGE), self.element, procs
