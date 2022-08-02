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


    def __init__(self, data):

        self.name = data["name"]
        self.img = Assets.loadImage(data["image"])

        self.function = data["function"]
