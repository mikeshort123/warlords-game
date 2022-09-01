from src.utils.vector import Vector
from src.projectiles.bullet import Bullet
from src.entities.enemyFactory import EnemyFactory
from src.tiles.grid import Grid
from src.uis.uiFrame import UIFrame
from src.uis.pauseMenu import PauseMenu
from src.states.state import State
from src.utils.particleManager import ParticleManager
from src.events.eventManager import EventManager
from src.events.eventType import EventType

class World(UIFrame):


    def __init__(self,player,cam):

        self.grid = Grid()

        self.player = player
        self.cam = cam

        self.particles = ParticleManager()

        self.enemyFactory = EnemyFactory()
        self.enemyFactory.loadEnemy("res/enemies/ball_guy.json")
        self.enemyFactory.loadEnemy("res/enemies/robot.json")

        self.entities = []
        self.projectiles = []

        self.entities.append(self.enemyFactory.generateEnemy("Ball Guy",player.pos.copy(), ai=True))
        self.entities.append(self.enemyFactory.generateEnemy("Robot",player.pos.copy() + Vector(0,2)))

        EventManager.register_events({
            EventType.PROJECTILE : self.add_projectile,
            EventType.EXPLOSION : self.activate_explosion
        })

    def tick(self,handler):

        if handler.getKeyChanged("PAUSE_GAME"):
            State.addFrame(PauseMenu())
            return

        self.particles.tick()

        self.player.tick(handler,self.grid)

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

        self.particles.render(renderer, self.cam)


    def add_projectile(self, projectile):
        self.projectiles.append(projectile)

    def activate_explosion(self, explosion):
        explosion.genEffect(self.particles)
        explosion.applyDamage(self.entities)
