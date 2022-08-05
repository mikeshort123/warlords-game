from src.animations.animationController import AnimationController

class AnimationGenerator:

    def __init__(self, data, scale):

        self.data = data
        self.scale = scale

    def newController(self):

        controller = AnimationController(self.scale)

        for animation in self.data["animations"]:
            controller.addAnimation(animation)

        return controller
