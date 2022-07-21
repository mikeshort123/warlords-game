from src.tiles.tile import Tile
from src.utils.vector import Vector
from src.entities.bullet import Bullet
from src.entities.enemy import Enemy
from src.tiles.grid import Grid

class World():



    def __init__(self,player,cam):

        self.grid = Grid()

        self.player = player
        self.cam = cam

        self.entities = []

        self.entities.append(Enemy("res/enemies/ball_guy.json",player.pos.copy()))
        self.entities.append(Enemy("res/enemies/robot.json",player.pos.copy() + Vector(0,2)))

    def tick(self,handler):

        self.player.tick(handler,self.grid,self.makeBullet)

        for entity in self.entities:
            entity.tick(handler,self.grid,self.entities,self.player)
            if not entity.alive:
                self.entities.remove(entity)


    def render(self,renderer):

        self.cam.moveTo(self.player)

        self.grid.render(renderer,self.cam)

        for entity in self.entities:
            entity.render(renderer,self.cam)

        self.player.render(renderer,self.cam)



    def makeBullet(self,handler,colour):
        toMouse = (handler.getMousePos() - Vector(320,240)) / 64
        self.entities.append(Bullet(self.player.pos.copy(),toMouse.normalize(),colour))
