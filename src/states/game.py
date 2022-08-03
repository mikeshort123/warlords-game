from src.utils.assets import Assets
from src.cam import Cam
from src.world import World
from src.player.player import Player
from src.definitions.element import Element
from src.mods.mod import Mod

class Game:

    def __init__(self,handler):

        Assets.loadFont()
        Element.loadElementDefinitions("res/definitions/elements.json")
        Mod.loadMods("res/mods/mods.json")

        self.cam = Cam(0,0)
        self.player = Player(125//2,5)

        self.world = World(self.player,self.cam)

        self.frame_stack = [self.world]

    def tick(self,handler):

        self.frame_stack[-1].tick(handler)

    def render(self,renderer):

        self.frame_stack[0].render(renderer)
        if len(self.frame_stack) > 1:
            self.frame_stack[-1].render(renderer)

    def dropFrame(self):
        self.frame_stack.pop()

    def addFrame(self,frame):
        self.frame_stack.append(frame)
