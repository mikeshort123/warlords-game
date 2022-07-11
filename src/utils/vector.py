import math

class Vector():

    def __init__(self, *args):

        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            return

        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
            return

        self.x = 0
        self.y = 0

    def __add__(self,o):
        if isinstance(o, Vector):
            return Vector(self.x+o.x, self.y+o.y)
        return Vector(self.x+o, self.y+o)

    def __iadd__(self,o):
        if isinstance(o, Vector):
            self.x += o.x
            self.y += o.y
        else:
            self.x += o
            self.y += o
        return self

    def __sub__(self,o):
        if isinstance(o, Vector):
            return Vector(self.x-o.x, self.y-o.y)
        return Vector(self.x-o, self.y-o)

    def __isub__(self,o):
        if isinstance(o, Vector):
            self.x -= o.x
            self.y -= o.y
        else:
            self.x -= o
            self.y -= o
        return self

    def __mul__(self,o):
        if isinstance(o, Vector):
            return Vector(self.x*o.x, self.y*o.y)
        return Vector(self.x*o, self.y*o)

    def __imul__(self,o):
        if isinstance(o, Vector):
            self.x *= o.x
            self.y *= o.y
        else:
            self.x *= o
            self.y *= o
        return self

    def __truediv__(self,o):
        if isinstance(o, Vector):
            return Vector(self.x/o.x, self.y/o.y)
        return Vector(self.x/o, self.y/o)

    def __itruediv__(self,o):
        if isinstance(o, Vector):
            self.x /= o.x
            self.y /= o.y
        else:
            self.x /= o
            self.y /= o
        return self

    def __neg__(self):
        return Vector(-self.x,-self.y)

    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+"]"

    def __eq__(self,o):
        return self.x == o.x and self.y == o.y

    def copy(self):
        return Vector(self.x,self.y)

    def normalize(self,m=1):
        d = self.length()
        if d > 0:
            self.x = m * self.x / d
            self.y = m * self.y / d
        return self

    def list(self):
        return [self.x,self.y]

    def int(self):
        self.x = int(self.x)
        self.y = int(self.y)
        return self

    def isZero(self):
        return (self.x == 0) and (self.y == 0)

    def atan(self):
        return math.atan2(self.y,self.x)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotate(self,t):
        cos = math.cos(t)
        sin = math.sin(t)
        x = cos*self.x + sin*self.y
        y = cos*self.y - sin*self.x
        return Vector(x,y)
