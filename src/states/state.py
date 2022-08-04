from src.utils.assets import Assets

class State():

    state = None

    @staticmethod
    def setState(StateType):
        Assets.flush()
        State.state = StateType()

    @staticmethod
    def tick(handler):
        State.state.tick(handler)

    @staticmethod
    def render(renderer):
        State.state.render(renderer)

    @staticmethod
    def addFrame(frame):
        State.state.frameManager.addFrame(frame)

    @staticmethod
    def dropFrame():
        State.state.frameManager.dropFrame()
