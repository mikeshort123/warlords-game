from src.utils.vector import Vector
from src.animations.animation import Animation

class AnimationController:

    class Part:

        def __init__(self):

            self.offset = Vector()
            self.theta = 0


    def __init__(self, parts):

        self.parts = {part : AnimationController.Part() for part in parts}
        self.animations = []

        self.t = 0

    def addAnimation(self,data):

        self.animations.append(Animation(data["part"],data["condition"],data["angle"],data["offset"]))

    def tick(self):
        self.t += 1


    def getPart(self,part_name):

        part = AnimationController.Part()

        for animation in self.animations:

            if animation.part == part_name and animation.condition():

                part.offset += animation.offset(self.t)
                part.theta += animation.angle(self.t)

        return part
