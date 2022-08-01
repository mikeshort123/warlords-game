

class Semiauto:



    def __init__(self,firerate):

        self.firerate = firerate
        self.prefire_delta = self.firerate // 3
        self.count = self.firerate

        self.prefire = False



    def tick(self,handler):

        if self.count <= self.prefire_delta and handler.getKeyChanged("SHOOT"):
            self.prefire = True

        if self.count == 0:

            if self.prefire:
                self.count = self.firerate
                self.prefire = False
                return True

        else:

            self.count -= 1

        return False
