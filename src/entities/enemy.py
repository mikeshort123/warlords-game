import json
from src.utils.assets import Assets

class Enemy:

    def __init__(self, fn, pos):

        with open(fn) as f:
            data = json.load(f)

        model_path = data["model"]

        self.model = Assets.loadModel(model_path)

        self.pos = pos

        self.alive = True

    def tick(self,handler,grid): return

    def render(self,renderer,cam):

        self.model.render(renderer,self.pos,cam)
