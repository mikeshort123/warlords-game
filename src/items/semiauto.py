

class Semiauto:

    def __init__(self,rof):

        self.rof = rof

        self.count = rof

    def tick(self,handler,bulletGenerator):

        if self.count == 0:

            if handler.getKeyChanged("SHOOT"):
                bulletGenerator(handler,(255,0,255))
                self.count = self.rof

        else:

            self.count -= 1
