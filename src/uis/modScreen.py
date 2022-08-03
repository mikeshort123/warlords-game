import pygame

from src.utils.assets import Assets
from src.states.state import State
from src.mods.mod import Mod
from src.utils.hitbox import Hitbox
from src.uis.uiFrame import UIFrame
from src.utils.vector import Vector

class ModScreen(UIFrame):

    DISPLAY_WIDTH = 3

    def __init__(self, item):

        self.blankslot = Assets.loadImage("res/textures/uis/modslot.png")

        self.slots = item.mods
        self.slotHitboxes = [Hitbox(56 + 192*(i%ModScreen.DISPLAY_WIDTH), 56 + 128*(i//ModScreen.DISPLAY_WIDTH), 144, 96) for i in range(len(self.slots))]

        self.mod_list = Mod.mod_list
        self.modHitboxes = [Hitbox(56 + 150*i, 360, 144, 96) for i in range(len(self.mod_list))]

        self.mod_bar_hitbox = Hitbox(56, 360, 528, 96)

        self.leftscroll_hitbox = Hitbox(36, 360, 20, 96)
        self.rightscroll_hitbox = Hitbox(584, 360, 20, 96)

        self.mod_pixel_offset = 0

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY"):
            State.state.dropFrame()
            return

        if handler.getKeyPressed("SELECT"):
            pos = handler.getMousePos()

            if self.leftscroll_hitbox.isInside(pos) and self.mod_pixel_offset > 0:
                self.mod_pixel_offset -= 8
                return

            if self.rightscroll_hitbox.isInside(pos) and self.mod_pixel_offset < len(self.mod_list) * 150 - 528 - 6:
                self.mod_pixel_offset += 8
                return

        if handler.getKeyChanged("SELECT"):
            pos = handler.getMousePos()

            for i, hitbox in enumerate(self.slotHitboxes):
                if hitbox.isInside(pos):
                    self.slots[i] = None
                    return

            if self.mod_bar_hitbox.isInside(pos):

                offset = Vector(self.mod_pixel_offset,0)

                for mod, hitbox in zip(self.mod_list, self.modHitboxes):
                    if hitbox.isInside(pos + offset):

                        if mod in self.slots: continue # dont put duplicate mods in

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

        pygame.draw.rect(renderer.display,(80,80,80),(36, 360, 20, 96))
        pygame.draw.rect(renderer.display,(80,80,80),(584, 360, 20, 96))

        for slot, hitbox in zip(self.slots, self.slotHitboxes):

            if slot:
                renderer.drawImage(slot.img,hitbox.ax,hitbox.ay)
            else:
                renderer.drawImage(self.blankslot,hitbox.ax,hitbox.ay)

        mod_bar = pygame.Surface((528,96), pygame.SRCALPHA)

        for i, (mod, hitbox) in enumerate(zip(self.mod_list, self.modHitboxes)):

            mod_bar.blit(mod.img, (i*150 - self.mod_pixel_offset, 0))

        renderer.drawImage(mod_bar, 56, 360)
