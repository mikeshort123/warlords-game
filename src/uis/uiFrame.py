from src.states.state import State

class UIFrame:

    def __init__(self,tick,render):

        self.tick = tick
        self.render = render

        self.moves = {}

    def load(self,handler):

        for key, frame in self.moves.items():
            handler.bindButtonFunction(UIFrame.getTransferFunction(frame),key)

    def addMove(self,key,frame):
        self.moves[key] = frame


    @staticmethod
    def getTransferFunction(frame):

        def transferFunction(handler):

            handler.clearBinds()
            State.setFrame(frame)
            frame.load(handler)

        return transferFunction
