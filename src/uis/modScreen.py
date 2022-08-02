import pygame

from src.utils.assets import Assets
from src.states.state import State
from src.mods.mod import Mod
from src.utils.hitbox import Hitbox

class ModScreen:

    def __init__(self, item):

        self.item = item

        self.blankslot = Assets.loadImage("res/textures/uis/modslot.png")

        self.slots = [None for i in range(6)]
        self.slotHitboxes = [Hitbox(56 + 192*(i%3), 56 + 128*(i//3), 144, 96) for i in range(6)]

        self.mod_list = Mod.loadMods("res/mods/mods.json")
        self.modHitboxes = [Hitbox(56 + 150*i, 360, 144, 96) for i in range(len(self.mod_list))]

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY"):
            State.state.dropFrame()

        if handler.getKeyChanged("SELECT"):
            pos = handler.getMousePos()

            for i, hitbox in enumerate(self.slotHitboxes):
                if hitbox.isInside(pos):
                    self.slots[i] = None

            for mod, hitbox in zip(self.mod_list, self.modHitboxes):
                if hitbox.isInside(pos):

                    index = self.getFirstEmptySlot()
                    if index != None:
                        self.slots[index] = mod


    def getFirstEmptySlot(self):

        for i, slot in enumerate(self.slots):
            if slot == None: return i

        else:
            return None


    def render(self,renderer):

        renderer.drawAlphaBackground((0,0,0),200)

        for slot, hitbox in zip(self.slots, self.slotHitboxes):

            if slot:
                renderer.drawImage(slot.img,hitbox.ax,hitbox.ay)
            else:
                renderer.drawImage(self.blankslot,hitbox.ax,hitbox.ay)

        for mod, hitbox in zip(self.mod_list, self.modHitboxes):

            renderer.drawImage(mod.img,hitbox.ax,hitbox.ay)
