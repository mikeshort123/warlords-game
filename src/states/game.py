from src.cam import Cam
from src.world import World
from src.player.player import Player
from src.uis.frameManager import FrameManager


class Game:

    def __init__(self):


        self.cam = Cam(0,0)
        self.player = Player(125//2,5)

        self.world = World(self.player,self.cam)

        self.frameManager = FrameManager(self.world)


    def tick(self,handler):

        self.frameManager.getActiveFrame().tick(handler)



    def render(self,renderer):

        if self.frameManager.getFrameCount() > 1:
            self.frameManager.getFrameAt(0).render(renderer)

        self.frameManager.getActiveFrame().render(renderer)
