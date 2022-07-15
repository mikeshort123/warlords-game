import pygame, json
from src.element import Element
from src.utils.assets import Assets
from src.models.weaponModel import WeaponModel
from src.models.playerModel import PlayerModel

class Item:

    class ItemInfo:

        def __init__(self,item):

            self.img = pygame.Surface((300,200))
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

        def draw(self,screen):
            screen.blit(self.img,(self.x,self.y))

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

        self.img = Assets.loadImage("blah",weapon_data["icon"])

        frame_data = weapon_data["frame"]
        with open(frame_data["type"],"r", encoding="utf8") as f:
            component_details = json.load(f)

        self.info = Item.ItemInfo(self)

        if weapon_data["slot"] == 3:
            self.model = PlayerModel(weapon_data["model"])
        else:
            self.model = WeaponModel(weapon_data["model"])



    def drawIcon(self,screen,x,y):
        screen.blit(self.img, (x,y))

    def getInfo(self,x,y):
        return self.info.setpos(x,y)
