from src.states.state import StateTemplate
from src.utils.assets import Assets
from src.cam import Cam
from src.world import World
from src.player.player import Player

class Game(StateTemplate):

    def __init__(self):

        Assets.loadImage("inventory","res/textures/uis/inventory.png")

        self.cam = Cam(0,0)
        self.player = Player(125/2,5)

        self.world = World(self.player)



    def tick(self,handler):

        self.world.tick(handler)


    def render(self,renderer):

        self.world.render(renderer,self.cam)
