from src.animations.animationController import AnimationController

class AnimationGenerator:

    def __init__(self,data,parts):

        self.data = data
        self.parts = parts

    def newController(self):

        controller = AnimationController(self.parts)

        for animation in self.data["animations"]:
            controller.addAnimation(animation)

        return controller
