from src.utils.vector import Vector
from src.entities.bullet import Bullet
from src.entities.enemyFactory import EnemyFactory
from src.tiles.grid import Grid
from src.uis.uiFrame import UIFrame

class World(UIFrame):


    def __init__(self,player,cam):

        self.grid = Grid()

        self.player = player
        self.cam = cam

        self.enemyFactory = EnemyFactory()
        self.enemyFactory.loadEnemy("res/enemies/ball_guy.json")
        self.enemyFactory.loadEnemy("res/enemies/robot.json")

        self.entities = []
        self.projectiles = []

        self.entities.append(self.enemyFactory.generateEnemy("Ball Guy",player.pos.copy()))
        self.entities.append(self.enemyFactory.generateEnemy("Robot",player.pos.copy() + Vector(0,2)))


    def tick(self,handler):

        self.player.tick(handler,self.grid,self.makeBullet)

        for projectile in self.projectiles:
            projectile.tick(self.grid,self.entities)
            if not projectile.alive:
                self.projectiles.remove(projectile)

        for entity in self.entities:
            entity.tick(self.grid,self.player)
            if entity.health <= 0:
                self.entities.remove(entity)


    def render(self,renderer):

        self.cam.moveTo(self.player)

        self.grid.render(renderer,self.cam)

        for entity in self.entities:
            entity.render(renderer,self.cam)

        self.player.render(renderer,self.cam)

        for projectile in self.projectiles:
            projectile.render(renderer,self.cam)



    def makeBullet(self, handler, colour, guy, damageProfileGenerator):
        toMouse = (handler.getMousePos() - Vector(320,240)) / 64
        self.projectiles.append(Bullet(self.player.pos.copy(), toMouse.normalize(), colour, guy, damageProfileGenerator))
