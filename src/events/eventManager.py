

class EventManager:

    events = []

    class Event:

        def __init__(self, type, package):
            self.type = type
            self.package = package

    @staticmethod
    def addEvent(type, package):

        EventManager.events.append(EventManager.Event(type, package))

    @staticmethod
    def get():

        e = EventManager.events
        EventManager.events = []
        return e
