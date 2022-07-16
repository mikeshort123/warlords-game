from src.states.state import State

class UIFrame:

    def __init__(self,tick,render):

        self.tick = tick
        self.render = render

        self.moves = {}
        self.eventBinds = {}

    def load(self,handler):

        for key, frame in self.moves.items():
            handler.bindButtonFunction(UIFrame.getTransferFunction(frame),key)

        for key, func in self.eventBinds.items():
            handler.bindClickFunction(func,key)

    def addMove(self,key,frame):
        self.moves[key] = frame

    def addBind(self,key,func):
        self.eventBinds[key] = func


    @staticmethod
    def getTransferFunction(frame):

        def transferFunction(handler):

            handler.clearBinds()
            State.setFrame(frame)
            frame.load(handler)

        return transferFunction
