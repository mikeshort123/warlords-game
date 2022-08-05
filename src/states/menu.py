from src.states.game import Game
from src.utils.assets import Assets
from src.uis.menu.mainMenu import MainMenu
from src.uis.frameManager import FrameManager

class Menu:

    def __init__(self):

        self.frameManager = FrameManager(MainMenu())


    def tick(self,handler):

        self.frameManager.getActiveFrame().tick(handler)


    def render(self,renderer):

        self.frameManager.getActiveFrame().render(renderer)
