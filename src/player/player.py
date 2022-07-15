import pygame
from src.utils.assets import Assets
from src.tiles.tile import Tile
from src.uis.inventory import Inventory
from src.models.playerModel import PlayerModel
from src.utils.vector import Vector
from src.models.weaponModel import WeaponModel

class Player():

    speed = 0.1
    width = 0.7
    height = 0.9

    def __init__(self,x,y):

        self.pos = Vector(x,y)

        self.model = PlayerModel("res/models/streetwear.json")

        self.primary = WeaponModel("res/models/rusty-iron.json")
        self.special = WeaponModel("res/models/bad-news.json")
        self.melee = WeaponModel("res/models/headsmans-axe.json")

        self.inventory = Inventory("res/save.json")

    def tick(self,handler,grid):

        #self.inventory.tick(handler)
        #if self.inventory.active: return

        n = Vector()

        if handler.getKey("UP"):
            n.y -= 1

        if handler.getKey("DOWN"):
            n.y += 1

        if handler.getKey("LEFT"):
            n.x -= 1

        if handler.getKey("RIGHT"):
            n.x += 1

        n.normalize(m=Player.speed)

        self.model.tick(handler,n)


        if self.checkCornerCollisions(self.pos.x+n.x,self.pos.y,grid): self.pos.x += n.x
        if self.checkCornerCollisions(self.pos.x,self.pos.y+n.y,grid): self.pos.y += n.y

        if handler.getKey("1"):
            self.model.weaponModel = self.primary
        if handler.getKey("2"):
            self.model.weaponModel = self.special
        if handler.getKey("3"):
            self.model.weaponModel = self.melee




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

        return Tile.getTile(grid[tx][ty]).solid


    def render(self,renderer,cam):

        self.model.render(renderer,self.pos,cam)

        #self.inventory.render(renderer)
