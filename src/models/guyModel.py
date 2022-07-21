import pygame

from src.models.model import Model
from src.utils.vector import Vector


class GuyModel:


    def __init__(self,model_data,modelTexture):

        self.scale = model_data["scale"]

        self.parts = []
        levels = {} # store level to order parts in order they should be drawn

        for part in model_data["parts"]:

            imgCentre = Vector(part["centre"])
            imgPos = Vector(part["pos"])
            imgSize = Vector(part["size"])

            name = part["name"]
            levels[name] = part["level"]

            centre = (imgPos - imgCentre + imgSize/2) / self.scale
            offset = Vector(part["offset"]) / self.scale

            size = imgSize / self.scale

            img = pygame.Surface(imgSize.list(), pygame.SRCALPHA)
            img.blit(modelTexture, (0, 0), (imgPos.x, imgPos.y, imgSize.x, imgSize.y))

            self.parts.append([name,Model(img,size,centre,offset)])

        self.parts.sort(key=lambda p : levels[p[0]]) # sort parts by level


    def render(self,renderer,pos,cam,animator):

        for name, part in self.parts:
            part.render(renderer,pos,cam,temp=animator.getPart(name))
