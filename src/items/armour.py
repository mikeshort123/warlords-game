import json

from src.models.playerModel import PlayerModel

class Armour:

    def __init__(self, wielder, item):

        self.wielder = wielder
        self.model = PlayerModel(item.model_path)

        self.element = item.element


    def tick(self, handler):
        return
