

class EventManager:

    events = {}

    @staticmethod
    def register_events(events):

        EventManager.events = events

    @staticmethod
    def trigger_event(type, package):

        EventManager.events[type](package)
