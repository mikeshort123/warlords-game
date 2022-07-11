import json,pygame

from src.utils.assets import Assets
from src.utils.vector import Vector
from src.models.model import Model

class WeaponModel():


    def __init__(self,fn,handoffset):

        with open(fn) as f:
            data = json.load(f)

        img = Assets.loadImage(data["imgname"],data["imgsrc"])

        scale = data["scale"]
        handle = Vector(data["handle"]) / scale
        barrel = Vector(data["barrel"]) / scale
        self.direction = Vector(data["direction"]).normalize()


        if "body_offset" in data:
            self.body_offset = Vector(data["body_offset"]) / scale
        else:
            self.body_offset = Vector()


        self.ws = (barrel - handle).rotate(self.direction.atan()) #vector from handle to barrel

        size = Vector(img.get_size()) / scale
        offset = handoffset.rotate(-self.direction.atan()) - handle + (size / 2)

        self.lefthandle = None
        if "left_hand" in data:
            self.lefthandle = handoffset + ((Vector(data["left_hand"])/scale) - handle).rotate(self.direction.atan())

        self.model = Model(img,size,offset)


    def render(self,renderer,pos,cam,theta = 0):
        self.model.render(renderer,pos,cam,theta=theta+self.direction.atan(),untoffset=self.body_offset)
