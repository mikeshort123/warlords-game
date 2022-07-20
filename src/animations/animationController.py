from src.utils.vector import Vector

class AnimationController:

    class Part:

        def __init__(self):

            self.offset = Vector()
            self.theta = 0

    def __init__(self):

        self.parts = {"right_hand" : AnimationController.Part()}

    def tick(self):
        self.parts["right_hand"].theta -= 0.1

    def getPart(self,part):

        if part in self.parts:
            return self.parts[part]

        return AnimationController.Part()
