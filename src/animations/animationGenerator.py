from src.animations.animationController import AnimationController

class AnimationGenerator:

    def __init__(self,data,parts,scale):

        self.data = data
        self.parts = parts
        self.scale = scale

    def newController(self):

        controller = AnimationController(self.parts,self.scale)

        for animation in self.data["animations"]:
            controller.addAnimation(animation)

        return controller
