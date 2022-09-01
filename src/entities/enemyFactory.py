import json

from src.utils.vector import Vector
from src.entities.enemy import Enemy
from src.utils.assets import Assets

class EnemyFactory:

    class Generator:

        def __init__(self,data):

            self.model_path = data["model"]
            model, _ = Assets.loadModel(self.model_path)

            self.maxhealth = data["health"]
            self.hitbox_size = Vector(data["hitbox_size"]) / model.scale
            self.hitbox_offset = (Vector(data["hitbox_offset"]) / model.scale) - (self.hitbox_size / 2)


    def __init__(self):

        self.generators = {}


    def loadEnemy(self,fp):

        with open(fp) as f:
            data = json.load(f)

        name = data["name"]
        self.generators[name] = EnemyFactory.Generator(data)


    def generateEnemy(self,name,pos,ai=False):

        return Enemy(pos,self.generators[name],ai=ai)
