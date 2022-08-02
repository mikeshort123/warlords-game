import json

from src.utils.assets import Assets

class Mod:

    @staticmethod
    def loadMods(fn):

        mod_list = []

        with open(fn) as f:
            data = json.load(f)

            for mod_data in data["mods"]:
                mod_list.append(Mod(mod_data))

        return mod_list


    def __init__(self, data):

        self.name = data["name"]
        self.img = Assets.loadImage(data["image"])
