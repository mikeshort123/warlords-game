

class Fullauto:

    def __init__(self,rof):

        self.rof = rof

        self.count = rof

    def tick(self,handler,bulletGenerator):

        if self.count == 0:

            if handler.getKeyPressed("SHOOT"):
                bulletGenerator(handler)
                self.count = self.rof

        else:

            self.count -= 1