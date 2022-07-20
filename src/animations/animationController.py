from src.utils.vector import Vector

class AnimationController:

    class Part:

        def __init__(self):

            self.offset = Vector()
            self.theta = 0

    class Animation:

        def __init__(self,part,angle=0,offset=0):

            self.part = part
            self.angle = angle
            self.offset = offset

            self.condition = lambda x : True

    def __init__(self, parts):

        self.parts = {part : AnimationController.Part() for part in parts}
        self.animations = []

    def addAnimation(self,data):

        self.animations.append(AnimationController.Animation(data["part"],angle=data["d_angle"]))

    def tick(self):

        for animation in self.animations:

            if animation.condition(None):
                part = self.parts[animation.part]
                part.offset += animation.offset
                part.theta += animation.angle



    def getPart(self,part):

        return self.parts[part]
