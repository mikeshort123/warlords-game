import json

from src.items.fullauto import Fullauto
from src.items.semiauto import Semiauto
from src.models.weaponModel import WeaponModel

class Weapon:

    def __init__(self, wielder, item):

        self.wielder = wielder

        self.model = WeaponModel(item.model_path)
        self.component = Weapon.generateFrame(item.frame_data,item.stats,item.element)


    def tick(self, handler, bulletGenerator):
        self.component.tick(handler, bulletGenerator)


    @staticmethod
    def generateFrame(frame,stats,element):

        with open(frame["type"]) as f:
            frame_data = json.load(f)

        frame_ref = {
            "gun-auto" : Fullauto,
            "gun-semiauto" : Semiauto
        }

        component_type = frame_ref[frame_data["type"]]

        subtype = frame_data["subtypes"][frame["subtype"]]

        return component_type(subtype,stats,element)
