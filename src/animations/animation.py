

class Animation:

    def __init__(self,part,condition,angle,offset):

        self.part = part

        self.condition = Animation.getConditionFunction(condition)

        self.angle = Animation.getMovementFunction(angle)
        self.offset = Animation.getMovementFunction(offset)


    @staticmethod
    def getMovementFunction(data):

        if data["type"] == "movement.constant": return lambda : data["value"]


    @staticmethod
    def getConditionFunction(data):

        if data["type"] == "condition.constant": return lambda : data["value"]
