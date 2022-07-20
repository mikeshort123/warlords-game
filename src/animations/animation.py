

class Animation:

    def __init__(self,part,condition,angle,offset):

        self.part = part

        self.condition = Animation.getConditionFunction(condition)

        self.angle = Animation.getMovementFunction(angle)
        self.offset = Animation.getMovementFunction(offset)




    @staticmethod
    def getMovementFunction(data):

        if data["type"] == "movement.fixed": return lambda t : data["value"]
        elif data["type"] == "movement.constant": return lambda t : data["value"] * t


    @staticmethod
    def getConditionFunction(data):

        if data["type"] == "condition.constant": return lambda : data["value"]
