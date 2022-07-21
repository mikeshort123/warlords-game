import json

class Element:

    elements = []

    @staticmethod
    def loadElementDefinitions(fn):

        with open(fn,"r", encoding="utf8") as f:
            data = json.load(f)

        for element in data["elements"]:
            Element.elements.append(Element(element))

        Element.elements.sort(key = lambda e : e.id)


    @staticmethod
    def getElement(id):
        return Element.elements[id]


    def __init__(self,data):
        self.name = data["name"]
        self.id = data["id"]
        self.colour = data["colour"]
