from src.utils.vector import Vector
from src.animations.animation import Animation

class AnimationController:

    class Part:

        def __init__(self):

            self.offset = Vector()
            self.theta = 0


    def __init__(self, parts, scale):

        self.variables = {}

        self.animations = []
        self.scale = scale

        self.t = 0

    def addAnimation(self,data):

        self.animations.append(Animation(data,self.variables))

    def tick(self):
        self.t += 1


    def setVariable(self,name,value):
        self.variables[name] = value


    def getPart(self,part_name):

        part = AnimationController.Part()

        for animation in self.animations:

            if animation.part == part_name and animation.condition():

                part.offset += animation.offset(self.t)
                part.theta += animation.angle(self.t)

        part.offset /= self.scale

        return part
