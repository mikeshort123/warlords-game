from src.utils.vector import Vector
from src.animations.blank import Blank

class Hand(Blank):

    def __init__(self):

        Blank.__init__(self)

    def tick(self, handler):

        toMouse = handler.getMousePos() - Vector(320,240)

        self.theta = - toMouse.atan()
