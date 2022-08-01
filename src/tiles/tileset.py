import json
from src.utils.assets import Assets

class Tileset:

    class Tile:

        def __init__(self,data):

            self.name = data["name"]
            self.texture = Assets.loadImage(data["imgsrc"])
            self.solid = data["solid"]


    def __init__(self,fp):

        self.tiles = Tileset.loadTileset(fp)


    def getTile(self,i):

        return self.tiles[i]


    @staticmethod
    def loadTileset(fp):

        with open(fp) as f:
            data = json.load(f)

        return [Tileset.Tile(tData) for tData in data["tiles"]]
