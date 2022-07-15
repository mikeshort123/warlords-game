from src.states.state import StateTemplate
from src.utils.assets import Assets
from src.cam import Cam
from src.world import World
from src.player.player import Player
from src.element import Element
from src.uis.uiFrame import UIFrame

class Game(StateTemplate):

    def __init__(self,handler):

        StateTemplate.__init__(self)

        Assets.loadImage("inventory","res/textures/uis/inventory.png")
        Assets.loadFont()
        Element.loadElementDefinitions("res/elements.json")

        self.cam = Cam(0,0)
        self.player = Player(125/2,5)

        self.world = World(self.player)

        baseFrame = UIFrame(self.world.tick,self.world.render)
        inventoryFrame = UIFrame(self.player.inventory.tick,self.player.inventory.render)

        baseFrame.addMove("OPEN_INVENTORY",inventoryFrame)
        inventoryFrame.addMove("OPEN_INVENTORY",baseFrame)

        self.setFrame(baseFrame)
        baseFrame.load(handler)





    def tick(self,handler):

        #self.world.tick(handler)
        self.uiFrame.tick(handler)


    def render(self,renderer):

        #self.world.render(renderer,self.cam)
        self.uiFrame.render(renderer,self.cam)
