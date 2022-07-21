from src.states.state import State

class UIFrame:

    def __init__(self,tickMethod,renderMethod):

        self.tickMethod = tickMethod
        self.renderMethod = renderMethod

        self.moves = {}


    def addMove(self,key,frame):
        self.moves[key] = frame


    def tick(self,handler):
        for key, frame in self.moves.items():
            if handler.getKeyChanged(key):
                State.setFrame(frame)
                return

        self.tickMethod(handler)

    def render(self,renderer):
        self.renderMethod(renderer)
