import math,pygame,json

from src.models.model import Model
from src.utils.vector import Vector


class PlayerModelTwo:

    defaultRig = {
        "head" : Vector(0,-12),
        "body" : Vector(0,0),
        "left_hand" : Vector(-19,7),
        "right_hand" : Vector(25,0),
        "left_foot" : Vector(-10,22),
        "right_foot" : Vector(10,22),
    }


    def __init__(self,model_data,modelTexture):

        self.parts = {}

        self.scale = model_data["scale"]

        for part, values in model_data["parts"].items():

            imgCentre = Vector(values["centre"])
            imgPos = Vector(values["pos"])
            imgSize = Vector(values["size"])

            offset = (imgPos - imgCentre + imgSize/2 + PlayerModelTwo.defaultRig[part]) / self.scale

            size = imgSize / self.scale

            img = pygame.Surface(imgSize.list(), pygame.SRCALPHA)
            img.blit(modelTexture, (0, 0), (imgPos.x, imgPos.y, imgSize.x, imgSize.y))

            self.parts[part] = Model(img,size,offset)



    #def tick(self, handler):



    def render(self,renderer,pos,cam):

        self.parts["body"].render(renderer,pos,cam)
        self.parts["left_foot"].render(renderer,pos,cam)
        self.parts["right_foot"].render(renderer,pos,cam)

        self.parts["left_hand"].render(renderer,pos,cam)
        self.parts["right_hand"].render(renderer,pos,cam)

        self.parts["head"].render(renderer,pos,cam)
