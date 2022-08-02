import pygame

from src.utils.assets import Assets
from src.states.state import State

class ModScreen:

    def __init__(self, item):

        self.item = item

    def tick(self,handler):

        if handler.getKeyChanged("CLOSE_INVENTORY"):

            State.state.dropFrame()


    def render(self,renderer):

        renderer.drawAlphaBackground((0,0,0),200)

        pygame.draw.rect(renderer.display,self.item.element.colour,(100,100,144,96))
