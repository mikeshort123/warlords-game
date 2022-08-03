import json

from src.utils.assets import Assets

class Mod:

    mod_list = []

    @staticmethod
    def loadMods(fn):

        Mod.mod_list = []

        with open(fn) as f:
            data = json.load(f)

            for mod_data in data["mods"]:
                Mod.mod_list.append(Mod(mod_data))


    @staticmethod
    def getMods(isArmour):
        f = filter(lambda m: (m.slot == 3) == isArmour, Mod.mod_list)
        return list(f)


    def __init__(self, data):

        self.name = data["name"]
        self.img = Assets.loadImage(data["image"])

        self.function = data["function"]

        self.slot = data["slot"]
