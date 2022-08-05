from src.utils.assets import Assets

class State():

    state = None

    states = {}

    @staticmethod
    def setState(name):
        Assets.flush()
        State.state = State.states[name]()

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

    @staticmethod
    def registerState(state, name):
        State.states[name] = state
