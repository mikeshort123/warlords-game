import pygame

from src.utils.assets import Assets
from src.states.state import State
from src.mods.mod import Mod
from src.utils.hitbox import Hitbox
from src.uis.uiFrame import UIFrame
from src.utils.vector import Vector
from src.definitions.inventorySlotNames import InventorySlotNames

class ModScreen(UIFrame):

    MOD_WIDTH = 144
    MOD_HEIGHT = 96

    DISPLAY_WIDTH = 3

    HORIZONTAL_SLOT_GAP = 48
    VERTICAL_SLOT_GAP = 32

    HORIZONTAL_SLOT_SPACING = HORIZONTAL_SLOT_GAP + MOD_WIDTH
    VERTICAL_SLOT_SPACING = VERTICAL_SLOT_GAP + MOD_HEIGHT

    HORIZONTAL_SLOT_OFFSET = (640 - DISPLAY_WIDTH*HORIZONTAL_SLOT_SPACING + HORIZONTAL_SLOT_GAP) // 2
    VERTICAL_SLOT_OFFSET = HORIZONTAL_SLOT_OFFSET

    MOD_BAR_WIDTH = DISPLAY_WIDTH*HORIZONTAL_SLOT_SPACING - HORIZONTAL_SLOT_GAP
    MOD_BAR_HEIGHT = MOD_HEIGHT

    MOD_BAR_HORIZONTAL_OFFSET = (640 - MOD_BAR_WIDTH) // 2
    MOD_BAR_VERTICAL_OFFSET = 360

    MOD_GAP = 6
    MOD_SPACING = MOD_GAP + MOD_WIDTH

    SCROLL_BUTTON_WIDTH = 20
    LEFT_SCROLL_BUTTON_OFFSET = MOD_BAR_HORIZONTAL_OFFSET - SCROLL_BUTTON_WIDTH
    RIGHT_SCROLL_BUTTON_OFFSET = MOD_BAR_HORIZONTAL_OFFSET + MOD_BAR_WIDTH

    SCROLL_SPEED = 8

    def __init__(self, item):

        self.blankslot = Assets.loadImage("res/textures/uis/modslot.png")

        self.slots = item.mods
        self.slotHitboxes = [
            Hitbox(
                ModScreen.HORIZONTAL_SLOT_OFFSET + ModScreen.HORIZONTAL_SLOT_SPACING*(i%ModScreen.DISPLAY_WIDTH),
                ModScreen.VERTICAL_SLOT_OFFSET + ModScreen.VERTICAL_SLOT_SPACING*(i//ModScreen.DISPLAY_WIDTH),
                ModScreen.MOD_WIDTH,
                ModScreen.MOD_HEIGHT
            ) for i in range(len(self.slots))
        ]

        self.mod_list = Mod.getMods(item.slot is InventorySlotNames.ARMOUR)

        self.modHitboxes = [
            Hitbox(
                ModScreen.MOD_BAR_HORIZONTAL_OFFSET + ModScreen.MOD_SPACING*i,
                ModScreen.MOD_BAR_VERTICAL_OFFSET,
                ModScreen.MOD_WIDTH,
                ModScreen.MOD_HEIGHT
            ) for i in range(len(self.mod_list))
        ]

        self.mod_bar_hitbox = Hitbox(
            ModScreen.MOD_BAR_HORIZONTAL_OFFSET,
            ModScreen.MOD_BAR_VERTICAL_OFFSET,
            ModScreen.MOD_BAR_WIDTH,
            ModScreen.MOD_BAR_HEIGHT
        )

        self.left_scroll_hitbox = Hitbox(
            ModScreen.LEFT_SCROLL_BUTTON_OFFSET,
            ModScreen.MOD_BAR_VERTICAL_OFFSET,
            ModScreen.SCROLL_BUTTON_WIDTH,
            ModScreen.MOD_BAR_HEIGHT
        )
        self.left_scroll_image = Assets.loadImage("res/textures/uis/left_scroll.png")
        self.right_scroll_hitbox = Hitbox(
            ModScreen.RIGHT_SCROLL_BUTTON_OFFSET,
            ModScreen.MOD_BAR_VERTICAL_OFFSET,
            ModScreen.SCROLL_BUTTON_WIDTH,
            ModScreen.MOD_BAR_HEIGHT
        )
        self.right_scroll_image = Assets.loadImage("res/textures/uis/right_scroll.png")

        self.mod_pixel_offset = 0
        self.max_scroll = len(self.mod_list)*ModScreen.MOD_SPACING - ModScreen.MOD_BAR_WIDTH - ModScreen.MOD_GAP

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY") or handler.getKeyChanged("CLOSE_MENU"):
            State.dropFrame()
            return

        if handler.getKeyPressed("SELECT"):
            pos = handler.getMousePos()

            if self.left_scroll_hitbox.isInside(pos) and self.mod_pixel_offset > 0:
                self.mod_pixel_offset -= ModScreen.SCROLL_SPEED
                return

            if self.right_scroll_hitbox.isInside(pos) and self.mod_pixel_offset < self.max_scroll:
                self.mod_pixel_offset += ModScreen.SCROLL_SPEED
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

        for slot, hitbox in zip(self.slots, self.slotHitboxes):

            if slot:
                hitbox.drawImage(renderer,slot.img)
            else:
                hitbox.drawImage(renderer,self.blankslot)

        mod_bar = pygame.Surface((ModScreen.MOD_BAR_WIDTH, ModScreen.MOD_BAR_HEIGHT), pygame.SRCALPHA)

        for i, mod in enumerate(self.mod_list):

            mod_bar.blit(mod.img, (i*ModScreen.MOD_SPACING - self.mod_pixel_offset, 0))

        renderer.drawUIImage(mod_bar, ModScreen.MOD_BAR_HORIZONTAL_OFFSET, ModScreen.MOD_BAR_VERTICAL_OFFSET)

        self.left_scroll_hitbox.drawImage(renderer,self.left_scroll_image)
        self.right_scroll_hitbox.drawImage(renderer,self.right_scroll_image)
