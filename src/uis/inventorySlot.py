from src.items.item import Item
from src.utils.assets import Assets
from src.items.weapon import Weapon
from src.states.state import State
from src.uis.modScreen import ModScreen
from src.utils.hitbox import Hitbox

class InventorySlot:

    ITEM_SIZE = 64
    ITEM_SPACING = 10
    WIDTH = 3
    HEIGHT = 3

    def __init__(self,player,data,x,y,isWeaponSlot):

        self.blankimg = Assets.loadImage("res/textures/uis/itemslot.png")

        self.x = x
        self.y = y

        self.selected_bound = Hitbox(self.x,self.y,InventorySlot.ITEM_SIZE,InventorySlot.ITEM_SIZE)
        self.pocket_bound = Hitbox(self.x,self.y+InventorySlot.ITEM_SIZE,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.WIDTH,(InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)*InventorySlot.HEIGHT)

        self.slots = [Item(item_data) for item_data in data]

        self.player = player

        self.isWeaponSlot = isWeaponSlot # temporary to tell difference between weapon and armour

        self.active = self.getSelectedItem().generateActiveObject(self.player)


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
                    renderer.drawUIImage(self.blankimg,x,y)


    def getSelectedItem(self):

        if len(self.slots) <= 0:
            return None
        return self.slots[0]


    def mouse_in_bounds(self,pos,active):
        return self.selected_bound.isInside(pos) or (active and self.pocket_bound.isInside(pos))


    def pickItem(self,pos): # if an item is clicked, swap it to be active

        index = self.mousePosToItem(pos)
        if index <= 0: return

        self.slots[0],self.slots[index] = self.slots[index],self.slots[0]

        self.active = self.getSelectedItem().generateActiveObject(self.player)


    def openModScreen(self,pos): # if an item is clicked, swap it to be active

        index = self.mousePosToItem(pos)
        if index == -1: return

        mod_menu = ModScreen(self.slots[index])
        State.addFrame(mod_menu)



    def checkHoveredItem(self,pos): # get item mouse is hovering over

        index = self.mousePosToItem(pos)
        if index == -1: return None

        return self.slots[index].getInfo(pos.x,pos.y)


    def mousePosToItem(self,pos): # turn a mouse pos into an item index if hovering over an item

        if self.selected_bound.isInside(pos): return 0

        i = (pos.x-self.x) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING)
        j = (pos.y-self.y) // (InventorySlot.ITEM_SIZE+InventorySlot.ITEM_SPACING) - 1

        if 0 <= i < InventorySlot.WIDTH and 0 <= j < InventorySlot.HEIGHT:
            index = i + j*InventorySlot.WIDTH + 1
            if len(self.slots) > index:
                return index
        return -1
