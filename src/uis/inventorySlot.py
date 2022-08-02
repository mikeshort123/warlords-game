import pygame

from src.items.item import Item
from src.utils.assets import Assets
from src.items.weapon import Weapon
from src.states.state import State
from src.uis.modScreen import ModScreen
from src.uis.uiFrame import UIFrame

class InventorySlot:

    ITEM_SIZE = 64
    ITEM_SPACING = 10
    WIDTH = 3
    HEIGHT = 3

    def __init__(self,player,data,x,y,isWeaponSlot):

        self.blankimg = Assets.loadImage("res/textures/uis/itemslot.png")

        self.x = x
        self.y = y

        self.selected_bound = pygame.Rect(self.x,self.y,InventorySlot.ITEM_SIZE,InventorySlot.ITEM_SIZE)
        self.pocket_bound = pygame.Rect(self.x,self.y+InventorySlot.ITEM_SIZE,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.WIDTH,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.HEIGHT)

        self.slots = [Item(item_data) for item_data in data]

        self.player = player

        if isWeaponSlot:
            self.active = self.tempGenerateGunObject()


    def render(self,renderer,active):

        if len(self.slots) > 0:
            self.slots[0].drawIcon(renderer,self.x,self.y)

        if not active: return
        for i in range(InventorySlot.WIDTH):
            for j in range(InventorySlot.HEIGHT):
                index = i + j*InventorySlot.WIDTH + 1
                x,y = self.x + i * (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING), self.y + (j+1) * (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)

                if len(self.slots) > index:
                    self.slots[index].drawIcon(renderer,x,y)
                else:
                    renderer.drawImage(self.blankimg,x,y)


    def getSelectedItem(self):

        if len(self.slots) <= 0:
            return None
        return self.slots[0]


    def tempGenerateGunObject(self):

        item = self.getSelectedItem()
        return Weapon(self.player,item)


    def mouse_in_bounds(self,handler,active):
        (x,y) = handler.getMousePos().list()
        return self.selected_bound.collidepoint(x, y) or (active and self.pocket_bound.collidepoint(x, y))


    def pickItem(self,handler): # if an item is clicked, swap it to be active
        (x,y) = handler.getMousePos().list()
        index = self.mousePosToItem(x,y)
        if index == -1: return
        self.slots[0],self.slots[index] = self.slots[index],self.slots[0]

        self.active = self.tempGenerateGunObject() # generate new weapon object


    def openModScreen(self,handler): # if an item is clicked, swap it to be active
        (x,y) = handler.getMousePos().list()

        if self.selected_bound.collidepoint(x, y):
            index = 0
        else:
            index = self.mousePosToItem(x,y)
            if index == -1: return

        mod_menu = ModScreen()

        mod_frame = UIFrame(mod_menu.tick,mod_menu.render)
        State.state.addFrame(mod_frame)



    def checkHoveredItem(self,handler): # get item mouse is hovering over
        (x,y) = handler.getMousePos().list()

        if self.selected_bound.collidepoint(x, y):
            index = 0
        else:
            index = self.mousePosToItem(x,y)
            if index == -1: return None

        return self.slots[index].getInfo(x,y)


    def mousePosToItem(self,x,y): # turn a mouse pos into an item index if hovering over an item
        i = (x-self.x) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)
        j = (y-self.y) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING) - 1

        if 0 <= i < InventorySlot.WIDTH and 0 <= j < InventorySlot.HEIGHT:
            index = i + j*InventorySlot.WIDTH + 1
            if len(self.slots) > index:
                return index
        return -1
