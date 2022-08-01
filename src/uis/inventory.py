import json

from src.uis.inventorySlot import InventorySlot
from src.definitions.inventorySlotNames import InventorySlotNames

class Inventory:

    def __init__(self,player,fn):

        with open(fn, "r", encoding="utf8") as f:
            data = json.load(f)

        self.primary = InventorySlot(player,data["primary"],50,50,True);
        self.special = InventorySlot(player,data["special"],160,50,True);
        self.melee = InventorySlot(player,data["melee"],270,50,True);
        self.armour = InventorySlot(player,data["armour"],380,50,False);

        self.active_display = None
        self.weapon_info = None

    def tick(self,handler):

        if self.primary.mouse_in_bounds(handler,self.active_display == self.primary): self.active_display = self.primary
        elif self.special.mouse_in_bounds(handler,self.active_display == self.special): self.active_display = self.special
        elif self.melee.mouse_in_bounds(handler,self.active_display == self.melee): self.active_display = self.melee
        elif self.armour.mouse_in_bounds(handler,self.active_display == self.armour): self.active_display = self.armour
        else: self.active_display = None

        if self.active_display:
            if handler.getKeyChanged("SELECT"):
                self.active_display.pickItem(handler)
            self.weapon_info = self.active_display.checkHoveredItem(handler)
        else:
            self.weapon_info = None

    def render(self,renderer):

        renderer.drawAlphaBackground((0,0,0),180)

        self.primary.render(renderer,self.active_display == self.primary)
        self.special.render(renderer,self.active_display == self.special)
        self.melee.render(renderer,self.active_display == self.melee)
        self.armour.render(renderer,self.active_display == self.armour)

        if self.weapon_info: self.weapon_info.draw(renderer)


    def getActiveItem(self,slot):

        mapping = {
            InventorySlotNames.PRIMARY : self.primary,
            InventorySlotNames.SPECIAL : self.special,
            InventorySlotNames.MELEE : self.melee,
            InventorySlotNames.ARMOUR : self.armour
        }

        return mapping[slot].active
