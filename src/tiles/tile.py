import json
from src.utils.assets import Assets

class Tile():

    tiles = []

    @staticmethod
    def getTile(i):

        return Tile.tiles[i]

    @staticmethod
    def loadTileset(fn):

        Tile.flush()

        with open(fn, encoding="utf8") as f:
            data = json.load(f)

        for index, tData in enumerate(data["tiles"]):

            Tile.tiles.append(Tile(tData))



    @staticmethod
    def flush():

        Tile.tiles.clear()


    def __init__(self,d):

        self.name = d["name"]
        self.texture = Assets.loadImage(d["imgsrc"])
        self.solid = d["solid"]
