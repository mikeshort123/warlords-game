import json,pygame

from src.uis.inventorySlot import InventorySlot

class Inventory:

    def __init__(self,fn):

        with open(fn,"r") as f:
            data = json.load(f)

        self.primary = InventorySlot(data["primary"],50,50);
        self.special = InventorySlot(data["special"],160,50);
        self.melee = InventorySlot(data["melee"],270,50);
        self.armour = InventorySlot(data["armour"],380,50);

        self.active_display = None
        self.weapon_info = None

    def tick(self,handler):

        if self.primary.mouse_in_bounds(handler,self.active_display == self.primary): self.active_display = self.primary
        elif self.special.mouse_in_bounds(handler,self.active_display == self.special): self.active_display = self.special
        elif self.melee.mouse_in_bounds(handler,self.active_display == self.melee): self.active_display = self.melee
        elif self.armour.mouse_in_bounds(handler,self.active_display == self.armour): self.active_display = self.armour
        else: self.active_display = None

        if self.active_display:
            handler.bindClickFunction(self.active_display.pickItem,0)
            self.weapon_info = self.active_display.checkHoveredItem(handler)
        else:
            handler.bindClickFunction(None,0)
            self.weapon_info = None

    def render(self,renderer):

        s = pygame.Surface(renderer.display.get_size())
        s.set_alpha(180)
        s.fill((0,0,0))
        renderer.display.blit(s,(0,0))

        self.primary.render(renderer.display,self.active_display == self.primary)
        self.special.render(renderer.display,self.active_display == self.special)
        self.melee.render(renderer.display,self.active_display == self.melee)
        self.armour.render(renderer.display,self.active_display == self.armour)

        if self.weapon_info: self.weapon_info.draw(renderer.display)
