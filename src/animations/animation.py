import math

from src.utils.vector import Vector

class Animation:

    def __init__(self,data,variables):

        self.part = data["part"]

        self.condition = Animation.getConditionFunction(data["condition"],variables)

        self.angle = Animation.getMovementFunction(data["angle"],variables)
        self.x_offset = Animation.getMovementFunction(data["x_offset"],variables)
        self.y_offset = Animation.getMovementFunction(data["y_offset"],variables)


    def offset(self,t):
        return Vector(self.x_offset(t),self.y_offset(t))


    @staticmethod
    def getMovementFunction(data,variables):

        if data["type"] == "movement.fixed": return lambda t : data["value"]
        elif data["type"] == "movement.constant": return lambda t : data["value"] * t
        elif data["type"] == "movement.none": return lambda t : 0
        elif data["type"] == "movement.variable":
            variables[data["name"]] = 0
            return lambda t : variables[data["name"]]
        elif data["type"] == "movement.sin": return lambda t : data["magnitude"] * math.sin(2*math.pi*t/data["period"])


    @staticmethod
    def getConditionFunction(data,variables):

        if data["type"] == "condition.on": return lambda : True
        elif data["type"] == "condition.boolean":
            variables[data["name"]] = True
            return lambda : variables[data["name"]]
