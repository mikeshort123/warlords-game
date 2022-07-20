import pygame

from src.models.model import Model
from src.utils.vector import Vector


class PlayerModelTwo:


    def __init__(self,model_data,modelTexture):

        self.parts = {}

        self.scale = model_data["scale"]

        for part, values in model_data["parts"].items():

            imgCentre = Vector(values["centre"])
            imgPos = Vector(values["pos"])
            imgSize = Vector(values["size"])

            centre = (imgPos - imgCentre + imgSize/2) / self.scale
            offset = Vector(values["offset"]) / self.scale

            size = imgSize / self.scale

            img = pygame.Surface(imgSize.list(), pygame.SRCALPHA)
            img.blit(modelTexture, (0, 0), (imgPos.x, imgPos.y, imgSize.x, imgSize.y))

            self.parts[part] = Model(img,size,centre,offset)


    def render(self,renderer,pos,cam,animator):

        self.parts["body"].render(renderer,pos,cam,temp=animator.getPart("body"))
        self.parts["left_foot"].render(renderer,pos,cam,temp=animator.getPart("left_foot"))
        self.parts["right_foot"].render(renderer,pos,cam,temp=animator.getPart("right_foot"))

        self.parts["left_hand"].render(renderer,pos,cam,temp=animator.getPart("left_hand"))
        self.parts["right_hand"].render(renderer,pos,cam,temp=animator.getPart("right_hand"))

        self.parts["head"].render(renderer,pos,cam,temp=animator.getPart("head"))
