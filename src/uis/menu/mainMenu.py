from src.utils.assets import Assets
from src.states.state import State
from src.uis.uiFrame import UIFrame


class MainMenu(UIFrame):

    def __init__(self):

        self.title = Assets.loadImage("res/textures/menu/titlescreen.png")


    def tick(self,handler):

        if handler.getKeyChanged("START"):
            State.setState("GAME")


    def render(self,renderer):

        renderer.drawUIImage(self.title,0,0)
