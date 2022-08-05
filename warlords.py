import pygame, sys

from src.utils.handler import Handler
from src.utils.renderer import Renderer
from src.states.state import State
from src.states.menu import Menu
from src.states.game import Game
from src.utils.assets import Assets
from src.definitions.element import Element
from src.mods.mod import Mod

def main():
    game = Main(640,480)
    game.run()


class Main():

    def __init__(self,x,y):

        pygame.init()

        self.MAXX = x
        self.MAXY = y

    def run(self):

        display = pygame.display.set_mode((self.MAXX,self.MAXY))
        clock = pygame.time.Clock()

        handler = Handler()
        renderer = Renderer(display)

        State.registerState(Menu,"MENU")
        State.registerState(Game,"GAME")

        State.setState("MENU")


        Assets.loadFont()
        Element.loadElementDefinitions("res/definitions/elements.json")
        Mod.loadMods("res/mods/mods.json")



        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                handler.handleEvent(event)

            display.fill((0,0,0))

            State.tick(handler)
            State.render(renderer)

            handler.reset()
            pygame.display.update()
            clock.tick(60)




if __name__ == "__main__": main()
