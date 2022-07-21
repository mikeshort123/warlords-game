import pygame, sys
from pygame.locals import *

from src.utils.handler import Handler
from src.utils.renderer import Renderer
from src.states.state import State
from src.states.menu import Menu

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

        State.setState(Menu,handler)



        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
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
