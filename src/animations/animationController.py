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

    def addAnimation(self,data):

        self.animations.append(Animation(data["part"],data["condition"],data["angle"],data["offset"]))

    def tick(self):

        for animation in self.animations:

            if animation.condition():
                part = self.parts[animation.part]
                part.offset += animation.offset()
                part.theta += animation.angle()



    def getPart(self,part):

        return self.parts[part]
