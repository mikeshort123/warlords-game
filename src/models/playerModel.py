import math,pygame,json

from src.models.model import Model
from src.models.weaponModel import WeaponModel
from src.utils.vector import Vector
from src.utils.assets import Assets


class PlayerModel():

    footPeriod = 4
    footMag = 3
    headMag = 0.5

    def __init__(self,fn):

        with open(fn) as f:
            data = json.load(f)

        modelTexture = Assets.loadImage(data["imgsrc"])

        self.parts = {}

        self.scale = data["scale"]

        for part, values in data["parts"].items():

            imgCentre = Vector(values["centre"])
            imgPos = Vector(values["pos"])
            imgSize = Vector(values["size"])

            centre = (imgPos - imgCentre + imgSize/2) / self.scale
            offset = Vector(values["offset"]) / self.scale

            size = imgSize / self.scale

            img = pygame.Surface(imgSize.list(), pygame.SRCALPHA)
            img.blit(modelTexture, (0, 0), (imgPos.x, imgPos.y, imgSize.x, imgSize.y))

            self.parts[part] = Model(img,size,centre,offset)

        self.v = Vector()
        self.t = 0

        self.weaponModel = None

        self.theta = 0


    def tick(self, handler, n, weaponModel):

        self.v = n * PlayerModel.headMag
        self.t += 1

        toMouse = handler.getGameMousePos()

        self.theta = toMouse.atan() # angle gun should be moved

        if weaponModel:

            dw = WeaponModel.weaponHandleOffset + weaponModel.ws # vector from body to barrel

            self.theta -= math.asin( dw.y / max(toMouse.length(),1) ) # angle between mouse and barrel from body






    def render(self,renderer,pos,cam,weaponModel):

        df = self.footMove()

        self.parts["body"].render(renderer,pos,cam)
        self.parts["left_foot"].render(renderer,pos,cam,d=df)
        self.parts["right_foot"].render(renderer,pos,cam,d=-df)

        self.parts["left_hand"].render(renderer,pos,cam)

        if weaponModel:
            weaponModel.render(renderer,pos,cam,theta = -self.theta)

            self.parts["right_hand"].render(renderer,pos,cam,theta = -self.theta)
        else:
            self.parts["right_hand"].render(renderer,pos,cam,theta = -self.theta)

        self.parts["head"].render(renderer,pos,cam,d=self.v)



    def footMove(self):

        if self.v.isZero():
            return Vector()


        if self.t >= PlayerModel.footPeriod * 4:
            self.t = 0

        y = self.t / PlayerModel.footPeriod

        if y > 1:
            y = 2 - y

        if y < -1:
            y = -2 - y

        return Vector(0,y*self.footMag/self.scale)
