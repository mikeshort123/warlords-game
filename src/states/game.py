from src.states.state import StateTemplate
from src.utils.assets import Assets
from src.cam import Cam
from src.world import World
from src.player.player import Player
from src.element import Element
from src.uis.uiFrame import UIFrame

class Game(StateTemplate):

    def __init__(self,handler):

        Assets.loadFont()
        Element.loadElementDefinitions("res/elements.json")

        self.cam = Cam(0,0)
        self.player = Player(125//2,5)

        self.world = World(self.player,self.cam)

        baseFrame = UIFrame(self.world.tick,self.world.render)
        inventoryFrame = UIFrame(self.player.inventory.tick,self.player.inventory.render)

        baseFrame.addMove("OPEN_INVENTORY",inventoryFrame)
        inventoryFrame.addMove("CLOSE_INVENTORY",baseFrame)

        StateTemplate.__init__(self,baseFrame,handler)

    def render(self,renderer):
        if self.uiFrame != self.baseFrame:
            self.baseFrame.render(renderer)
        self.uiFrame.render(renderer)
