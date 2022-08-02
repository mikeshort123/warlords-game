from src.utils.assets import Assets
from src.states.state import State

class ModScreen:

    def __init__(self):

        self.img = Assets.loadImage("res/textures/uis/itemslot.png")

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY"):

            State.state.dropFrame()


    def render(self,renderer):

        renderer.drawImage(self.img,30,50)
