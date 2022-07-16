from src.tiles.tile import Tile
from src.uis.inventory import Inventory
from src.utils.vector import Vector

class Player():

    speed = 0.1
    width = 0.7
    height = 0.9

    def __init__(self,x,y):

        self.pos = Vector(x,y)
        self.weapon_selection = "none"
        self.inventory = Inventory("res/save.json")

    def tick(self,handler,grid):

        n = Vector()

        if handler.getKeyPressed("UP"):
            n.y -= 1

        if handler.getKeyPressed("DOWN"):
            n.y += 1

        if handler.getKeyPressed("LEFT"):
            n.x -= 1

        if handler.getKeyPressed("RIGHT"):
            n.x += 1

        n.normalize(m=Player.speed)

        self.inventory.armour.slots[0].model.tick(handler,n,self.getWeaponModel())

        if self.checkCornerCollisions(self.pos.x+n.x,self.pos.y,grid): self.pos.x += n.x
        if self.checkCornerCollisions(self.pos.x,self.pos.y+n.y,grid): self.pos.y += n.y

        if handler.getKeyChanged("1"):
            self.weapon_selection = "primary"
        if handler.getKeyChanged("2"):
            self.weapon_selection = "special"
        if handler.getKeyChanged("3"):
            self.weapon_selection = "melee"




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

        self.inventory.armour.slots[0].model.render(renderer,self.pos,cam,self.getWeaponModel())

    def getWeapon(self):
        if self.weapon_selection == "primary": return self.inventory.primary.slots[0]
        if self.weapon_selection == "special": return self.inventory.special.slots[0]
        if self.weapon_selection == "melee": return self.inventory.melee.slots[0]
        return None

    def getWeaponModel(self):
        weapon = self.getWeapon()
        if weapon: return weapon.model
        return None
