import pygame

from src.uis.inventory import Inventory
from src.utils.vector import Vector
from src.definitions.inventorySlotNames import InventorySlotNames
from src.utils.assets import Assets
from src.definitions.element import Element
from src.states.state import State
from src.definitions.effects import Effects
from src.entities.dude import Dude

class Player(Dude):

    speed = 0.1
    width = 0.7
    height = 0.9

    def __init__(self, x, y):

        Dude.__init__(self,Vector(x,y))
        self.weapon_selection = InventorySlotNames.PRIMARY
        self.inventory = Inventory(self,"res/save.json")

        self.health = 100



    def tick(self,handler,grid,bulletGenerator):

        if handler.getKeyChanged("OPEN_INVENTORY"):
            State.addFrame(self.inventory)
            return

        self.modified_speed = Player.speed

        for name, effect in list(self.effects.items()):
            effect.tick(self)
            if effect.stacks <= 0:
                self.effects.pop(name)

        n = Vector()

        if handler.getKeyPressed("UP"):
            n.y -= 1

        if handler.getKeyPressed("DOWN"):
            n.y += 1

        if handler.getKeyPressed("LEFT"):
            n.x -= 1

        if handler.getKeyPressed("RIGHT"):
            n.x += 1

        n.normalize(m=self.modified_speed)

        self.inventory.getActiveItem(InventorySlotNames.ARMOUR).model.tick(handler,n,self.getWeaponModel())

        if self.checkCornerCollisions(self.pos.x+n.x,self.pos.y,grid): self.pos.x += n.x
        if self.checkCornerCollisions(self.pos.x,self.pos.y+n.y,grid): self.pos.y += n.y

        if handler.getKeyChanged("1"):
            self.weapon_selection = InventorySlotNames.PRIMARY
        if handler.getKeyChanged("2"):
            self.weapon_selection = InventorySlotNames.SPECIAL
        if handler.getKeyChanged("3"):
            self.weapon_selection = InventorySlotNames.MELEE

        if weapon := self.getWeapon():
            weapon.tick(handler, bulletGenerator)


    def applyDamage(self, damage, element):

        self.health -= damage


    def applyEffect(self, EffectType, amount):

        if EffectType not in self.effects:
            self.effects[EffectType] = EffectType()

        self.effects[EffectType].addStacks(amount)


    def getElementalEffects(self, element):

        effects = []

        for mod in self.inventory.slots[InventorySlotNames.ARMOUR].getSelectedItem().mods:

            if mod and mod.function["type"] == "ADD_ELEMENTAL_EFFECT" and element == Element.getElement(mod.function["element"]):

                effects.append(Effects.getEffectFromName(mod.function["add"]))


        return effects


    def checkCornerCollisions(self,x,y,grid):

        ax,ay = x - Player.width/2, y - Player.height/2
        bx,by = ax+Player.width,ay+Player.height

        if not self.checkPointCollision(ax,ay,grid):
            if not self.checkPointCollision(bx,ay,grid):
                if not self.checkPointCollision(ax,by,grid):
                    if not self.checkPointCollision(bx,by,grid):

                        return True

    def checkPointCollision(self,px,py,grid):

        tx = int(px+0.5)
        ty = int(py+0.5)

        return grid.getSolid(tx,ty)


    def render(self,renderer,cam):

        self.inventory.getActiveItem(InventorySlotNames.ARMOUR).model.render(renderer,self.pos,cam,self.getWeaponModel())

        words = Assets.font.render(str(self.health), True, (50,255,80))
        renderer.display.blit(words, (20, 20))

        for i, effect_type in enumerate(self.effects):

            pygame.draw.rect(renderer.display,effect_type.COLOUR,(5 + 25*i,45,20,20))

    def getWeapon(self):

        return self.inventory.getActiveItem(self.weapon_selection)

    def getWeaponModel(self):
        weapon = self.getWeapon()
        if weapon: return weapon.model
        return None
