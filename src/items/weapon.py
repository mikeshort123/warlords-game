import json

from src.items.fullauto import Fullauto
from src.items.semiauto import Semiauto
from src.models.weaponModel import WeaponModel

class Weapon:

    def __init__(self, wielder, item):

        self.wielder = wielder
        self.model = WeaponModel(item.model_path)

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

        firerate = 3600 // weapon_subtype_stats["firerate"] # convert rounds per minute into frames per round

        # use stats to set up weapons
        self.trigger = Trigger_type(firerate)

        self.damage = weapon_subtype_stats["damage"]
        self.status_chance = item.stats["element_chance"]
        self.element = item.element

        self.status_counter = 0


    def tick(self, handler, bulletGenerator):
        if self.trigger.tick(handler):
            bulletGenerator(handler, self.wielder, self.generateDamageProfile)




    def generateDamageProfile(self):

        self.status_counter += self.status_chance
        procs = int(self.status_counter)
        self.status_counter %= 1

        return self.damage, self.element, procs
