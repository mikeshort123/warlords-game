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
