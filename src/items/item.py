import pygame, json
from src.element import Element
from src.utils.assets import Assets

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

        with open(data["src"],"r") as f:
            weapon_data = json.load(f)

        self.name = weapon_data["name"]

        self.element = Element.getElement(weapon_data["element"])

        self.img = pygame.Surface((100,100))
        self.img.fill(self.element.colour)
        words = Assets.font.render(self.name, True, (255,255,255))
        self.img.blit(words, (0, 20))

        frame_data = weapon_data["frame"]
        with open(frame_data["type"],"r") as f:
            component_details = json.load(f)

        self.info = Item.ItemInfo(self)

        return

        if component_details["type"] == "gun-auto":
            self.component = Auto(component_details,frame_data["subtype"],weapon_data)
        elif component_details["type"] == "gun-semiauto":
            self.component = Semiauto(component_details,frame_data["subtype"],weapon_data)
        elif component_details["type"] == "melee":
            self.component = Melee(component_details,frame_data["subtype"],weapon_data)
        elif component_details["type"] == "armour":
            self.component = Armour(component_details,frame_data["subtype"],weapon_data)
        else:
            print("wtf")



    def drawIcon(self,screen,x,y):
        screen.blit(self.img, (x,y))

    def getInfo(self,x,y):
        return self.info.setpos(x,y)
