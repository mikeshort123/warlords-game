from src.uis.uiFrame import UIFrame
from src.utils.hitbox import Hitbox
from src.utils.assets import Assets
from src.states.state import State

class PauseMenu(UIFrame):

    def __init__(self):

        self.quit_hitbox = Hitbox(200,200,240,60)
        self.quit_image = Assets.loadImage("res/textures/uis/return_to_menu.png")

    def tick(self, handler):

        if handler.getKeyChanged("SELECT") and self.quit_hitbox.isInside(handler.getUIMousePos()):
            State.setState("MENU")
            return

        if handler.getKeyChanged("CLOSE_MENU"):
            State.dropFrame()

    def render(self, renderer):

        renderer.drawAlphaBackground((0,0,0),180)

        self.quit_hitbox.drawImage(renderer,self.quit_image)
