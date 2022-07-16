import pygame, json

from src.element import Element
from src.utils.assets import Assets
from src.models.weaponModel import WeaponModel
from src.models.playerModel import PlayerModel
from src.items.fullauto import Fullauto
from src.items.semiauto import Semiauto

class Item:

    class ItemInfo:

        WIDTH = 300
        HEIGHT = 200

        def __init__(self,item):

            self.img = pygame.Surface((Item.ItemInfo.WIDTH,Item.ItemInfo.HEIGHT))
            self.img.fill((130,0,100))
            words = Assets.font.render(item.name, True, (255,255,255))
            self.img.blit(words, (20, 20))
            pygame.draw.rect(self.img,item.element.colour,(275,5,20,20))

            for i in range(3):
                for j in range(2):
                    c = item.sockets[i + j*3].colour
                    if c:
                        pygame.draw.rect(self.img,c,(225+i*23,35+j*23,20,20))

            self.x = 0
            self.y = 0

        def draw(self,renderer):
            x = min(renderer.display.get_width()-Item.ItemInfo.WIDTH,self.x)
            y = min(renderer.display.get_height()-Item.ItemInfo.HEIGHT,self.y)
            renderer.drawImage(self.img,x,y)

        def setpos(self,x,y):
            self.x = x
            self.y = y
            return self

    def __init__(self,data):
        self.sockets = [Element.getElement(i) for i in data["sockets"]]

        with open(data["src"],"r", encoding="utf8") as f:
            weapon_data = json.load(f)

        self.name = weapon_data["name"]

        self.element = Element.getElement(weapon_data["element"])

        self.img = Assets.loadImage(weapon_data["icon"])

        frame_data = weapon_data["frame"]
        with open(frame_data["type"],"r", encoding="utf8") as f:
            component_details = json.load(f)

        self.info = Item.ItemInfo(self)

        if weapon_data["slot"] == 3:
            self.model = PlayerModel(weapon_data["model"])
        else:
            self.model = WeaponModel(weapon_data["model"])

        if weapon_data["slot"] == 0:
            self.component = Semiauto(10)
        if weapon_data["slot"] == 1:
            self.component = Fullauto(10)
        if weapon_data["slot"] == 2:
            self.component = Fullauto(20)


    def tick(self, handler, bulletGenerator):
        self.component.tick(handler, bulletGenerator)



    def drawIcon(self,renderer,x,y):
        renderer.drawImage(self.img,x,y)

    def getInfo(self,x,y):
        return self.info.setpos(x,y)
