import json

from src.uis.inventorySlot import InventorySlot
from src.definitions.inventorySlotNames import InventorySlotNames
from src.states.state import State
from src.uis.uiFrame import UIFrame

class Inventory(UIFrame):

    def __init__(self,player,fn):

        with open(fn, "r", encoding="utf8") as f:
            data = json.load(f)

        self.slots = {
            InventorySlotNames.PRIMARY : InventorySlot(player,data["primary"],50,50,True),
            InventorySlotNames.SPECIAL : InventorySlot(player,data["special"],160,50,True),
            InventorySlotNames.MELEE : InventorySlot(player,data["melee"],270,50,True),
            InventorySlotNames.ARMOUR : InventorySlot(player,data["armour"],380,50,False)
        }

        self.active_display = None
        self.weapon_info = None

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY") or handler.getKeyChanged("CLOSE_MENU"):
            State.dropFrame()
            return

        pos = handler.getUIMousePos()


        set = False

        for slot in self.slots.values():

            if slot.mouse_in_bounds(pos, self.active_display == slot):
                self.active_display = slot
                set = True

        if not set:
            self.active_display = None

        if self.active_display:
            if handler.getKeyChanged("MODIFY"):
                self.active_display.openModScreen(pos)
                return
            if handler.getKeyChanged("SELECT"):
                self.active_display.pickItem(pos)
            self.weapon_info = self.active_display.checkHoveredItem(pos)
        else:
            self.weapon_info = None

    def render(self,renderer):

        renderer.drawAlphaBackground((0,0,0),180)

        for slot in self.slots.values():

            slot.render(renderer, self.active_display == slot)

        if self.weapon_info: self.weapon_info.draw(renderer)


    def getActiveItem(self,slot):

        return self.slots[slot].active
