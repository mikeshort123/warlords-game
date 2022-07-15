from src.utils.assets import Assets

class State():

    state = None

    @staticmethod
    def setState(StateType,handler):
        Assets.flush()
        State.state = StateType(handler)

    @staticmethod
    def tick(handler):
        State.state.tick(handler)

    @staticmethod
    def render(renderer):
        State.state.render(renderer)

    @staticmethod
    def setFrame(frame):
        State.state.setFrame(frame)


class StateTemplate():

    def __init__(self):
        self.uiFrame = None

    def tick(self,handler): return
    def render(self,renderer) : return

    def setFrame(self,frame):
        self.uiFrame = frame
