from src.states.state import StateTemplate
from src.states.state import State
from src.states.game import Game
from src.utils.assets import Assets

class Menu(StateTemplate):

    def __init__(self,handler):

        self.title = Assets.loadImage("res/textures/menu/titlescreen.png")



    def tick(self,handler):

        if handler.getKeyChanged("START"):
            State.setState(Game,handler)


    def render(self,renderer):

        renderer.drawImage(self.title,0,0)
