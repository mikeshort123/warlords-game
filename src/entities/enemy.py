import json
from src.utils.assets import Assets
from src.animations.blank import Blank
from src.animations.feet import Feet
from src.animations.hand import Hand

class Enemy:

    def __init__(self, fn, pos):

        with open(fn) as f:
            data = json.load(f)

        model_path = data["model"]

        self.model = Assets.loadModel(model_path)

        self.pos = pos

        self.alive = True

        self.animations = {
            "head" : Blank(),
            "body" : Blank(),
            "left_hand" : Blank(),
            "right_hand" : Hand(),
            "left_foot" : Feet(-3/64,4),
            "right_foot" : Feet(3/64,4)
        }

    def tick(self,handler,grid):

        for _, part in self.animations.items():
            part.tick(handler)

    def render(self,renderer,cam):

        self.model.render(renderer,self.pos,cam,self.animations)
