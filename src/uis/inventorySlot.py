import pygame
from src.items.item import Item

class InventorySlot:

    ITEM_SIZE = 64
    ITEM_SPACING = 10
    WIDTH = 3
    HEIGHT = 3

    def __init__(self,data,x,y):

        self.x = x
        self.y = y

        self.selected_bound = pygame.Rect(self.x,self.y,InventorySlot.ITEM_SIZE,InventorySlot.ITEM_SIZE)
        self.pocket_bound = pygame.Rect(self.x,self.y+InventorySlot.ITEM_SIZE,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.WIDTH,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.HEIGHT)

        self.slots = [Item(item_data) for item_data in data]


    def render(self,screen,active):

        if len(self.slots) > 0:
            self.slots[0].drawIcon(screen,self.x,self.y)

        if not active: return
        for i in range(InventorySlot.WIDTH):
            for j in range(InventorySlot.HEIGHT):
                index = i + j*InventorySlot.WIDTH + 1
                x,y = self.x + i * (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING), self.y + (j+1) * (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)

                if len(self.slots) > index:
                    self.slots[index].drawIcon(screen,x,y)
                else:
                    pygame.draw.rect(screen,(100,100,100),(x,y,InventorySlot.ITEM_SIZE,InventorySlot.ITEM_SIZE))


    def mouse_in_bounds(self,handler,active):
        (x,y) = handler.getMousePos().list()
        return self.selected_bound.collidepoint(x, y) or (active and self.pocket_bound.collidepoint(x, y))


    def pickItem(self,handler):
        (x,y) = handler.getMousePos().list()
        index = self.mousePosToItem(x,y)
        if index == -1: return
        self.slots[0],self.slots[index] = self.slots[index],self.slots[0]


    def checkHoveredItem(self,handler):
        (x,y) = handler.getMousePos().list()

        if self.selected_bound.collidepoint(x, y):
            index = 0
        else:
            index = self.mousePosToItem(x,y)
            if index == -1: return None

        return self.slots[index].getInfo(x,y)


    def mousePosToItem(self,x,y):
        i = (x-self.x) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)
        j = (y-self.y) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING) - 1

        if 0 <= i < InventorySlot.WIDTH and 0 <= j < InventorySlot.HEIGHT:
            index = i + j*InventorySlot.WIDTH + 1
            if len(self.slots) > index:
                return index
        return -1
