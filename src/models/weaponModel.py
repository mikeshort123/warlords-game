import json,pygame

from src.utils.assets import Assets
from src.utils.vector import Vector
from src.models.model import Model

class WeaponModel():


    def __init__(self,fn):

        with open(fn, encoding="utf8") as f:
            data = json.load(f)

        img = Assets.loadImage(data["imgsrc"])

        scale = data["scale"]
        handle = Vector(data["handle"]) / scale
        barrel = Vector(data["barrel"]) / scale
        self.direction = Vector(data["direction"]).normalize()


        self.ws = (barrel - handle).rotate(self.direction.atan()) #vector from handle to barrel

        size = Vector(img.get_size()) / scale
        offset = (size / 2) - handle + Vector(25/64,0).rotate(-self.direction.atan())

        # DO STUFF WITH BODY OFFSETS AND LEFT HAND

        self.model = Model(img,size,offset)


    def render(self,renderer,pos,cam,theta = 0):
        self.model.render(renderer,pos,cam,theta=theta+self.direction.atan())
